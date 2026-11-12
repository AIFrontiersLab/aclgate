"""Role implementations. Components specialise one of these strategies."""

from permission_aware_retrieval.stages.answer import AnswerStage
from permission_aware_retrieval.stages.approval import ApprovalStage
from permission_aware_retrieval.stages.audit import AuditStage
from permission_aware_retrieval.stages.base import Stage, StageServices
from permission_aware_retrieval.stages.budget import BudgetStage
from permission_aware_retrieval.stages.cache import CacheStage
from permission_aware_retrieval.stages.enrich import EnrichStage
from permission_aware_retrieval.stages.fallback import FallbackStage
from permission_aware_retrieval.stages.ingest import IngestStage
from permission_aware_retrieval.stages.policy import PolicyStage
from permission_aware_retrieval.stages.retrieve import RetrieveStage
from permission_aware_retrieval.stages.score import ScoreStage

ROLE_CLASSES: dict[str, type[Stage]] = {
    "ingest": IngestStage,
    "retrieve": RetrieveStage,
    "enrich": EnrichStage,
    "score": ScoreStage,
    "cache": CacheStage,
    "policy": PolicyStage,
    "budget": BudgetStage,
    "approval": ApprovalStage,
    "fallback": FallbackStage,
    "audit": AuditStage,
    "answer": AnswerStage,
}

__all__ = ["ROLE_CLASSES", "Stage", "StageServices", *[cls.__name__ for cls in ROLE_CLASSES.values()]]
