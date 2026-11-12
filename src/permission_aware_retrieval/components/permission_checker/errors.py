"""Errors raised by Permission Checker. They are ``StageError`` subclasses so the
orchestrator applies its standard retry, breaker, and fallback semantics."""

from __future__ import annotations

from permission_aware_retrieval.kernel.errors import StageError


class PermissionCheckerError(StageError):
    code = "permission_checker_error"

    def __init__(self, message: str, *, retryable: bool = False, details: dict | None = None) -> None:
        super().__init__("permission_checker", message, retryable=retryable, details=details)


class PermissionCheckerContractViolation(PermissionCheckerError):
    code = "permission_checker_contract_violation"
