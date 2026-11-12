"""Pre- and post-conditions for Score Fusion Module.

Violations are defects, not transient faults, so they are raised as
non-retryable errors and surface as a degraded (or failed, if critical) stage.
"""

from __future__ import annotations

from permission_aware_retrieval.components.score_fusion_module.config import ScoreFusionModuleConfig
from permission_aware_retrieval.components.score_fusion_module.errors import ScoreFusionModuleContractViolation
from permission_aware_retrieval.components.score_fusion_module.models import ScoreFusionModuleInput


def validate_input(ctx, config: ScoreFusionModuleConfig) -> None:
    if len(ctx.candidates) > config.max_input_candidates:
        raise ScoreFusionModuleContractViolation(
            "too many candidates for score_fusion_module",
            details={"limit": config.max_input_candidates, "received": len(ctx.candidates)},
        )


def validate_output(ctx, before: ScoreFusionModuleInput, config: ScoreFusionModuleConfig) -> None:
    ids = [c.doc_id for c in ctx.candidates]
    if len(ids) != len(set(ids)):
        raise ScoreFusionModuleContractViolation("duplicate candidate ids after score_fusion_module")
    if not config.may_introduce_ids:
        unexpected = set(ids) - set(before.candidate_ids)
        if unexpected:
            raise ScoreFusionModuleContractViolation(
                "score_fusion_module introduced unknown candidates", details={"ids": sorted(unexpected)}
            )
    if config.enforce_sorted_output and not ctx.cache_hit:
        scores = [c.score for c in ctx.candidates]
        if scores != sorted(scores, reverse=True):
            raise ScoreFusionModuleContractViolation("score_fusion_module produced an unsorted ranking")
