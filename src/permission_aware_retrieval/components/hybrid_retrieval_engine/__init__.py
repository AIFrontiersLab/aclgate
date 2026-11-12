"""Hybrid Retrieval Engine.

Blends upstream prior scores with query-aware relevance and reorders candidates.
"""

from permission_aware_retrieval.components.hybrid_retrieval_engine.adapter import ROLE, build
from permission_aware_retrieval.components.hybrid_retrieval_engine.config import CONFIG, HybridRetrievalEngineConfig
from permission_aware_retrieval.components.hybrid_retrieval_engine.errors import HybridRetrievalEngineError
from permission_aware_retrieval.components.hybrid_retrieval_engine.service import HybridRetrievalEngineService

__all__ = ["CONFIG", "ROLE", "build", "HybridRetrievalEngineConfig", "HybridRetrievalEngineError", "HybridRetrievalEngineService"]
