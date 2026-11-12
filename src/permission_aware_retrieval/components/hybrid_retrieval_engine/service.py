"""Hybrid Retrieval Engine service.

Role: ``score``. Blends upstream prior scores with query-aware relevance and reorders candidates.

Responsibility (from the architecture specification):
    Blends upstream prior scores with query-aware relevance and reorders candidates.

The service specialises :class:`ScoreStage` and wraps it with this
component's contract checks, metrics, and per-run report.
"""

from __future__ import annotations

from permission_aware_retrieval.components.hybrid_retrieval_engine.config import CONFIG, HybridRetrievalEngineConfig
from permission_aware_retrieval.components.hybrid_retrieval_engine.models import HybridRetrievalEngineInput, HybridRetrievalEngineReport
from permission_aware_retrieval.components.hybrid_retrieval_engine.validators import validate_input, validate_output
from permission_aware_retrieval.stages.score import ScoreStage

METRIC_PREFIX = "component_hybrid_retrieval_engine"
RUNS = f"{METRIC_PREFIX}_runs_total"
CANDIDATES_OUT = f"{METRIC_PREFIX}_candidates_out"
REMOVED = f"{METRIC_PREFIX}_removed_total"


def record_metrics(metrics, report: HybridRetrievalEngineReport) -> None:
    if metrics is None:
        return
    metrics.inc(RUNS)
    metrics.observe(CANDIDATES_OUT, report.candidates_out)
    if report.removed:
        metrics.inc(REMOVED, len(report.removed))


class HybridRetrievalEngineService(ScoreStage):
    def __init__(self, services, config: HybridRetrievalEngineConfig = CONFIG) -> None:
        super().__init__(config.name, services, description=config.responsibility)
        self.config = config

    def process(self, ctx) -> None:
        validate_input(ctx, self.config)
        before = HybridRetrievalEngineInput.from_context(ctx)
        super().process(ctx)
        if ctx.halted and not ctx.candidates:
            report = HybridRetrievalEngineReport.diff(self.name, before, [], halted=True)
        else:
            validate_output(ctx, before, self.config)
            report = HybridRetrievalEngineReport.diff(self.name, before, [c.doc_id for c in ctx.candidates])
        ctx.metadata.setdefault("reports", {})[self.name] = report.to_dict()
        record_metrics(self.services.metrics, report)

    def describe(self) -> dict:
        info = super().describe()
        info.update({"display_name": self.config.display_name, "interface": self.config.interface})
        return info
