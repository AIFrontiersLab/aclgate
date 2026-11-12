"""Composition root: the only module that knows every concrete adapter.

``build_container`` turns ``Settings`` into a fully wired object graph. Tests and
embedders pass their own clock, corpus, or scorer to swap behaviour without
monkeypatching.
"""

from __future__ import annotations

from dataclasses import dataclass

from permission_aware_retrieval.adapters.outbound.audit_sink import InMemoryAuditSink
from permission_aware_retrieval.adapters.outbound.event_bus import InMemoryEventBus
from permission_aware_retrieval.adapters.outbound.jsonl_repository import JsonlRunRepository
from permission_aware_retrieval.adapters.outbound.lexical_scorer import LexicalScorer
from permission_aware_retrieval.adapters.outbound.memory_corpus import InMemoryCorpus
from permission_aware_retrieval.adapters.outbound.memory_repository import InMemoryRunRepository
from permission_aware_retrieval.adapters.outbound.ttl_cache import TTLRankingCache
from permission_aware_retrieval.application.bus import MessageBus
from permission_aware_retrieval.application.commands import ApproveRun, RunPipeline
from permission_aware_retrieval.application.handlers import (
    ApproveRunHandler,
    DescribePipelineHandler,
    GetRunHandler,
    ListRunsHandler,
    RunPipelineHandler,
)
from permission_aware_retrieval.application.orchestrator import Orchestrator
from permission_aware_retrieval.application.queries import DescribePipeline, GetRun, ListRuns
from permission_aware_retrieval.application.unit_of_work import UnitOfWork
from permission_aware_retrieval.config.settings import Settings
from permission_aware_retrieval.governance.approvals import ApprovalService
from permission_aware_retrieval.governance.budgets import BudgetGuard
from permission_aware_retrieval.governance.policy_engine import PolicyEngine
from permission_aware_retrieval.governance.redaction import Redactor
from permission_aware_retrieval.kernel.clock import Clock, SystemClock
from permission_aware_retrieval.observability.health import HealthRegistry
from permission_aware_retrieval.observability.logging import configure as configure_logging
from permission_aware_retrieval.observability.metrics import MetricsRegistry
from permission_aware_retrieval.observability.tracing import Tracer
from permission_aware_retrieval.plugins.hooks import HookManager
from permission_aware_retrieval.plugins.registry import StageRegistry
from permission_aware_retrieval.resilience.bulkhead import Bulkhead
from permission_aware_retrieval.resilience.circuit_breaker import BreakerState, CircuitBreaker
from permission_aware_retrieval.resilience.rate_limiter import KeyedRateLimiter
from permission_aware_retrieval.resilience.retry import RetryPolicy
from permission_aware_retrieval.stage_catalog import register_all
from permission_aware_retrieval.stages.base import StageServices
from permission_aware_retrieval.workflows.checkpoint import CheckpointStore


@dataclass
class Container:
    settings: Settings
    clock: Clock
    services: StageServices
    registry: StageRegistry
    stages: list
    orchestrator: Orchestrator
    runs: object
    bus: MessageBus
    health: HealthRegistry
    metrics: MetricsRegistry
    tracer: Tracer
    event_bus: InMemoryEventBus
    hooks: HookManager
    breakers: dict
    rate_limiter: KeyedRateLimiter
    checkpoints: CheckpointStore


def build_container(
    settings: Settings | None = None,
    *,
    clock: Clock | None = None,
    corpus=None,
    scorer=None,
    registry: StageRegistry | None = None,
) -> Container:
    settings = settings or Settings()
    clock = clock or SystemClock()
    configure_logging(settings.app.log_level)

    metrics = MetricsRegistry()
    tracer = Tracer(clock)
    event_bus = InMemoryEventBus()
    hooks = HookManager()
    checkpoints = CheckpointStore()
    cache = TTLRankingCache(settings.cache.capacity, settings.cache.ttl_seconds, clock=clock) if settings.cache.enabled else None

    gov = settings.governance
    services = StageServices(
        settings=settings,
        clock=clock,
        scorer=scorer or LexicalScorer(),
        corpus=corpus if corpus is not None else InMemoryCorpus(),
        cache=cache,
        audit=InMemoryAuditSink(),
        metrics=metrics,
        policy_engine=PolicyEngine(gov.role_clearances, gov.default_clearance),
        redactor=Redactor(),
        approvals=ApprovalService(),
        budget_guard=BudgetGuard(settings.budget.default_tokens, settings.budget.hard_limit_tokens),
    )

    if registry is None:
        registry = StageRegistry()
        register_all(registry)
    stages = registry.build(settings.pipeline.stages, services)

    res = settings.resilience
    breakers = {
        s.name: CircuitBreaker(s.name, failure_threshold=res.breaker_failure_threshold, reset_seconds=res.breaker_reset_seconds, clock=clock)
        for s in stages
    }
    orchestrator = Orchestrator(
        stages,
        clock=clock,
        tracer=tracer,
        metrics=metrics,
        event_bus=event_bus,
        hooks=hooks,
        checkpoints=checkpoints,
        cache=cache,
        breakers=breakers,
        retry=RetryPolicy(attempts=res.retry_attempts, base_delay=res.retry_base_delay, clock=clock),
        bulkhead=Bulkhead("pipeline", res.bulkhead_limit),
        stage_timeout_ms=settings.pipeline.stage_timeout_ms,
    )

    runs = JsonlRunRepository(settings.storage.path) if settings.storage.backend == "jsonl" else InMemoryRunRepository()
    run_handler = RunPipelineHandler(orchestrator, UnitOfWork(runs), checkpoints, clock)
    bus = MessageBus()
    bus.register(RunPipeline, run_handler)
    bus.register(ApproveRun, ApproveRunHandler(services.approvals, UnitOfWork(runs), run_handler))
    bus.register(GetRun, GetRunHandler(runs))
    bus.register(ListRuns, ListRunsHandler(runs))
    bus.register(DescribePipeline, DescribePipelineHandler(stages, registry))

    health = HealthRegistry()
    health.register("stages_loaded", lambda: len(stages) > 0)
    health.register("breakers_closed", lambda: all(b.state is not BreakerState.OPEN for b in breakers.values()))
    health.register("hooks_healthy", lambda: len(hooks.failures) == 0)

    return Container(
        settings=settings,
        clock=clock,
        services=services,
        registry=registry,
        stages=stages,
        orchestrator=orchestrator,
        runs=runs,
        bus=bus,
        health=health,
        metrics=metrics,
        tracer=tracer,
        event_bus=event_bus,
        hooks=hooks,
        breakers=breakers,
        rate_limiter=KeyedRateLimiter(res.rate_limit_per_second, res.rate_limit_burst, clock=clock),
        checkpoints=checkpoints,
    )
