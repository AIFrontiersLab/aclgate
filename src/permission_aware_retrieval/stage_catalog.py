"""Stage catalog for Permission-Aware Retrieval.

Declares the default stage order and registers every built-in and component stage
with the plugin registry. Imports of stage classes are deferred so configuration
modules can read ``DEFAULT_STAGE_ORDER`` without import cycles.
"""

from __future__ import annotations

DEFAULT_STAGE_ORDER = [
    "intake",
    "corpus_retrieval",
    "signal_enricher",
    "ranking_cache",
    "hybrid_retrieval_engine",
    "score_fusion_module",
    "graceful_fallback",
    "permission_checker",
    "token_budget_governor",
    "answer_assembly",
]

BUILTINS = {
    "intake": "ingest",
    "corpus_retrieval": "retrieve",
    "relevance_scoring": "score",
    "access_policy": "policy",
    "graceful_fallback": "fallback",
    "answer_assembly": "answer",
}

COMPONENTS = [
    {"name": 'Permission Checker', "slug": "permission_checker", "role": "policy", "origin": "spec"},
    {"name": 'Hybrid Retrieval Engine', "slug": "hybrid_retrieval_engine", "role": "score", "origin": "spec"},
    {"name": 'Score Fusion Module', "slug": "score_fusion_module", "role": "score", "origin": "spec"},
    {"name": 'Signal Enricher', "slug": "signal_enricher", "role": "enrich", "origin": "padded"},
    {"name": 'Ranking Cache', "slug": "ranking_cache", "role": "cache", "origin": "padded"},
    {"name": 'Token Budget Governor', "slug": "token_budget_governor", "role": "budget", "origin": "padded"},
]


def register_all(registry) -> None:
    from permission_aware_retrieval.components import COMPONENT_FACTORIES
    from permission_aware_retrieval.stages import ROLE_CLASSES

    for name, role in BUILTINS.items():
        cls = ROLE_CLASSES[role]
        registry.register(name, role, lambda services, cls=cls, name=name: cls(name, services), source="builtin")
    for name, (role, factory) in COMPONENT_FACTORIES.items():
        registry.register(name, role, factory, source="component")
