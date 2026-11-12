"""Ranking Cache.

Short-circuits repeated identical requests with a TTL-bounded ranking cache keyed by principal.
"""

from permission_aware_retrieval.components.ranking_cache.adapter import ROLE, build
from permission_aware_retrieval.components.ranking_cache.config import CONFIG, RankingCacheConfig
from permission_aware_retrieval.components.ranking_cache.errors import RankingCacheError
from permission_aware_retrieval.components.ranking_cache.service import RankingCacheService

__all__ = ["CONFIG", "ROLE", "build", "RankingCacheConfig", "RankingCacheError", "RankingCacheService"]
