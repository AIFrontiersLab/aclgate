"""Ports: the interfaces the application core requires from the outside world.

Adapters under ``permission_aware_retrieval.adapters`` implement these protocols. The core never
imports an adapter directly; the composition root (``container.py``) wires them.
"""

from permission_aware_retrieval.ports.audit import AuditSink
from permission_aware_retrieval.ports.cache import RankingCache
from permission_aware_retrieval.ports.corpus import CorpusRepository
from permission_aware_retrieval.ports.event_bus import EventBus
from permission_aware_retrieval.ports.repository import RunRepository
from permission_aware_retrieval.ports.scorer import RelevanceScorer

__all__ = ["AuditSink", "CorpusRepository", "EventBus", "RankingCache", "RelevanceScorer", "RunRepository"]
