"""Fallback role: when an upstream stage degraded, restore a safe ordering by prior score."""

from __future__ import annotations

from permission_aware_retrieval.domain.models import PipelineContext
from permission_aware_retrieval.stages.base import Stage


class FallbackStage(Stage):
    role = "fallback"

    def process(self, ctx: PipelineContext) -> None:
        if not ctx.degraded:
            ctx.decide(self.name, "noop", reason="healthy")
            return
        for cand in ctx.candidates:
            cand.score = cand.prior_score
        ctx.candidates.sort(key=lambda c: (-c.prior_score, c.doc_id))
        failed = [e.get("stage") for e in ctx.errors]
        ctx.decide(self.name, "restored_prior_order", failed_stages=failed)
