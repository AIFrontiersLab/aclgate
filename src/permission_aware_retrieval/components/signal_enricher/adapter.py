"""Port and registry adapter for Signal Enricher.

Interface from the architecture specification: ``process(ctx) -> None``
"""

from __future__ import annotations

from typing import Protocol

from permission_aware_retrieval.components.signal_enricher.config import CONFIG
from permission_aware_retrieval.components.signal_enricher.service import SignalEnricherService
from permission_aware_retrieval.domain.models import PipelineContext

ROLE = CONFIG.role


class SignalEnricherPort(Protocol):
    """Contract the orchestrator relies on."""

    name: str
    role: str

    def process(self, ctx: PipelineContext) -> None: ...

    def describe(self) -> dict: ...


def build(services) -> SignalEnricherService:
    return SignalEnricherService(services)
