"""Pre- and post-conditions for Hybrid Retrieval Engine.

Violations are defects, not transient faults, so they are raised as
non-retryable errors and surface as a degraded (or failed, if critical) stage.
"""

from __future__ import annotations

from permission_aware_retrieval.components.hybrid_retrieval_engine.config import HybridRetrievalEngineConfig
from permission_aware_retrieval.components.hybrid_retrieval_engine.errors import HybridRetrievalEngineContractViolation
from permission_aware_retrieval.components.hybrid_retrieval_engine.models import HybridRetrievalEngineInput


def validate_input(ctx, config: HybridRetrievalEngineConfig) -> None:
    if len(ctx.candidates) > config.max_input_candidates:
        raise HybridRetrievalEngineContractViolation(
            "too many candidates for hybrid_retrieval_engine",
            details={"limit": config.max_input_candidates, "received": len(ctx.candidates)},
        )


def validate_output(ctx, before: HybridRetrievalEngineInput, config: HybridRetrievalEngineConfig) -> None:
    ids = [c.doc_id for c in ctx.candidates]
    if len(ids) != len(set(ids)):
        raise HybridRetrievalEngineContractViolation("duplicate candidate ids after hybrid_retrieval_engine")
    if not config.may_introduce_ids:
        unexpected = set(ids) - set(before.candidate_ids)
        if unexpected:
            raise HybridRetrievalEngineContractViolation(
                "hybrid_retrieval_engine introduced unknown candidates", details={"ids": sorted(unexpected)}
            )
    if config.enforce_sorted_output and not ctx.cache_hit:
        scores = [c.score for c in ctx.candidates]
        if scores != sorted(scores, reverse=True):
            raise HybridRetrievalEngineContractViolation("hybrid_retrieval_engine produced an unsorted ranking")
