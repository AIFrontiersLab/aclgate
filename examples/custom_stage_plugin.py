"""Register a custom stage and insert it before answer assembly."""

from permission_aware_retrieval.config.settings import Settings
from permission_aware_retrieval.container import build_container
from permission_aware_retrieval.plugins.registry import StageRegistry
from permission_aware_retrieval.stage_catalog import register_all
from permission_aware_retrieval.stages.base import Stage


class FreshnessBoost(Stage):
    role = "score"

    def process(self, ctx):
        for cand in ctx.candidates:
            cand.score = round(cand.score + 0.05 * float(cand.metadata.get("recent", 0)), 6)
        ctx.candidates.sort(key=lambda c: (-c.score, c.doc_id))
        ctx.decide(self.name, "boosted")


registry = StageRegistry()
register_all(registry)
registry.register("freshness_boost", "score", lambda s: FreshnessBoost("freshness_boost", s), source="plugin")

settings = Settings()
settings.pipeline.stages.insert(len(settings.pipeline.stages) - 1, "freshness_boost")
container = build_container(settings, registry=registry)
print([s.name for s in container.stages])
