"""Port and registry adapter for Hybrid Retrieval Engine.

Interface from the architecture specification: ``process(ctx) -> None``
"""

from __future__ import annotations

from typing import Protocol

from permission_aware_retrieval.components.hybrid_retrieval_engine.config import CONFIG
from permission_aware_retrieval.components.hybrid_retrieval_engine.service import HybridRetrievalEngineService
from permission_aware_retrieval.domain.models import PipelineContext

ROLE = CONFIG.role


class HybridRetrievalEnginePort(Protocol):
    """Contract the orchestrator relies on."""

    name: str
    role: str

    def process(self, ctx: PipelineContext) -> None: ...

    def describe(self) -> dict: ...


def build(services) -> HybridRetrievalEngineService:
    return HybridRetrievalEngineService(services)
