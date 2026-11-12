"""Pre- and post-conditions for Permission Checker.

Violations are defects, not transient faults, so they are raised as
non-retryable errors and surface as a degraded (or failed, if critical) stage.
"""

from __future__ import annotations

from permission_aware_retrieval.components.permission_checker.config import PermissionCheckerConfig
from permission_aware_retrieval.components.permission_checker.errors import PermissionCheckerContractViolation
from permission_aware_retrieval.components.permission_checker.models import PermissionCheckerInput


def validate_input(ctx, config: PermissionCheckerConfig) -> None:
    if len(ctx.candidates) > config.max_input_candidates:
        raise PermissionCheckerContractViolation(
            "too many candidates for permission_checker",
            details={"limit": config.max_input_candidates, "received": len(ctx.candidates)},
        )


def validate_output(ctx, before: PermissionCheckerInput, config: PermissionCheckerConfig) -> None:
    ids = [c.doc_id for c in ctx.candidates]
    if len(ids) != len(set(ids)):
        raise PermissionCheckerContractViolation("duplicate candidate ids after permission_checker")
    if not config.may_introduce_ids:
        unexpected = set(ids) - set(before.candidate_ids)
        if unexpected:
            raise PermissionCheckerContractViolation(
                "permission_checker introduced unknown candidates", details={"ids": sorted(unexpected)}
            )
    if config.enforce_sorted_output and not ctx.cache_hit:
        scores = [c.score for c in ctx.candidates]
        if scores != sorted(scores, reverse=True):
            raise PermissionCheckerContractViolation("permission_checker produced an unsorted ranking")
