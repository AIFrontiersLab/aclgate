"""Score Fusion Module service.

Role: ``score``. Blends upstream prior scores with query-aware relevance and reorders candidates.

Responsibility (from the architecture specification):
    Blends upstream prior scores with query-aware relevance and reorders candidates.

The service specialises :class:`ScoreStage` and wraps it with this
component's contract checks, metrics, and per-run report.
"""

from __future__ import annotations

from permission_aware_retrieval.components.score_fusion_module.config import CONFIG, ScoreFusionModuleConfig
from permission_aware_retrieval.components.score_fusion_module.models import ScoreFusionModuleInput, ScoreFusionModuleReport
from permission_aware_retrieval.components.score_fusion_module.validators import validate_input, validate_output
from permission_aware_retrieval.stages.score import ScoreStage

METRIC_PREFIX = "component_score_fusion_module"
RUNS = f"{METRIC_PREFIX}_runs_total"
CANDIDATES_OUT = f"{METRIC_PREFIX}_candidates_out"
REMOVED = f"{METRIC_PREFIX}_removed_total"


def record_metrics(metrics, report: ScoreFusionModuleReport) -> None:
    if metrics is None:
        return
    metrics.inc(RUNS)
    metrics.observe(CANDIDATES_OUT, report.candidates_out)
    if report.removed:
        metrics.inc(REMOVED, len(report.removed))


class ScoreFusionModuleService(ScoreStage):
    def __init__(self, services, config: ScoreFusionModuleConfig = CONFIG) -> None:
        super().__init__(config.name, services, description=config.responsibility)
        self.config = config

    def process(self, ctx) -> None:
        validate_input(ctx, self.config)
        before = ScoreFusionModuleInput.from_context(ctx)
        super().process(ctx)
        if ctx.halted and not ctx.candidates:
            report = ScoreFusionModuleReport.diff(self.name, before, [], halted=True)
        else:
            validate_output(ctx, before, self.config)
            report = ScoreFusionModuleReport.diff(self.name, before, [c.doc_id for c in ctx.candidates])
        ctx.metadata.setdefault("reports", {})[self.name] = report.to_dict()
        record_metrics(self.services.metrics, report)

    def describe(self) -> dict:
        info = super().describe()
        info.update({"display_name": self.config.display_name, "interface": self.config.interface})
        return info
