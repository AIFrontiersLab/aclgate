"""Port and registry adapter for Permission Checker.

Interface from the architecture specification: ``process(ctx) -> None``
"""

from __future__ import annotations

from typing import Protocol

from permission_aware_retrieval.components.permission_checker.config import CONFIG
from permission_aware_retrieval.components.permission_checker.service import PermissionCheckerService
from permission_aware_retrieval.domain.models import PipelineContext

ROLE = CONFIG.role


class PermissionCheckerPort(Protocol):
    """Contract the orchestrator relies on."""

    name: str
    role: str

    def process(self, ctx: PipelineContext) -> None: ...

    def describe(self) -> dict: ...


def build(services) -> PermissionCheckerService:
    return PermissionCheckerService(services)
