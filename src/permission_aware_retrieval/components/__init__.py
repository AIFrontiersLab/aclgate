"""Concept-specific components. Each one specialises a stage role with its own
configuration, validation, metrics, and errors."""

from permission_aware_retrieval.components.hybrid_retrieval_engine import adapter as _hybrid_retrieval_engine
from permission_aware_retrieval.components.permission_checker import adapter as _permission_checker
from permission_aware_retrieval.components.ranking_cache import adapter as _ranking_cache
from permission_aware_retrieval.components.score_fusion_module import adapter as _score_fusion_module
from permission_aware_retrieval.components.signal_enricher import adapter as _signal_enricher
from permission_aware_retrieval.components.token_budget_governor import adapter as _token_budget_governor

COMPONENT_FACTORIES = {
    "permission_checker": (_permission_checker.ROLE, _permission_checker.build),
    "hybrid_retrieval_engine": (_hybrid_retrieval_engine.ROLE, _hybrid_retrieval_engine.build),
    "score_fusion_module": (_score_fusion_module.ROLE, _score_fusion_module.build),
    "signal_enricher": (_signal_enricher.ROLE, _signal_enricher.build),
    "ranking_cache": (_ranking_cache.ROLE, _ranking_cache.build),
    "token_budget_governor": (_token_budget_governor.ROLE, _token_budget_governor.build),
}
