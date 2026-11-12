"""Errors raised by Score Fusion Module. They are ``StageError`` subclasses so the
orchestrator applies its standard retry, breaker, and fallback semantics."""

from __future__ import annotations

from permission_aware_retrieval.kernel.errors import StageError


class ScoreFusionModuleError(StageError):
    code = "score_fusion_module_error"

    def __init__(self, message: str, *, retryable: bool = False, details: dict | None = None) -> None:
        super().__init__("score_fusion_module", message, retryable=retryable, details=details)


class ScoreFusionModuleContractViolation(ScoreFusionModuleError):
    code = "score_fusion_module_contract_violation"
