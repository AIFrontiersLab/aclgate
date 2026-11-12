"""Static configuration for the Permission Checker component."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PermissionCheckerConfig:
    name: str = "permission_checker"
    display_name: str = 'Permission Checker'
    role: str = "policy"
    interface: str = 'process(ctx) -> None'
    responsibility: str = 'Fail-closed tenant, clearance, and ACL filtering plus PII redaction.'
    max_input_candidates: int = 10_000
    may_introduce_ids: bool = False
    enforce_sorted_output: bool = False


CONFIG = PermissionCheckerConfig()
