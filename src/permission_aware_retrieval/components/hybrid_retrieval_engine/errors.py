"""Errors raised by Hybrid Retrieval Engine. They are ``StageError`` subclasses so the
orchestrator applies its standard retry, breaker, and fallback semantics."""

from __future__ import annotations

from permission_aware_retrieval.kernel.errors import StageError


class HybridRetrievalEngineError(StageError):
    code = "hybrid_retrieval_engine_error"

    def __init__(self, message: str, *, retryable: bool = False, details: dict | None = None) -> None:
        super().__init__("hybrid_retrieval_engine", message, retryable=retryable, details=details)


class HybridRetrievalEngineContractViolation(HybridRetrievalEngineError):
    code = "hybrid_retrieval_engine_contract_violation"
