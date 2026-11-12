"""Port and registry adapter for Ranking Cache.

Interface from the architecture specification: ``lookup(key) -> ranking | None``
"""

from __future__ import annotations

from typing import Protocol

from permission_aware_retrieval.components.ranking_cache.config import CONFIG
from permission_aware_retrieval.components.ranking_cache.service import RankingCacheService
from permission_aware_retrieval.domain.models import PipelineContext

ROLE = CONFIG.role


class RankingCachePort(Protocol):
    """Contract the orchestrator relies on."""

    name: str
    role: str

    def process(self, ctx: PipelineContext) -> None: ...

    def describe(self) -> dict: ...


def build(services) -> RankingCacheService:
    return RankingCacheService(services)
