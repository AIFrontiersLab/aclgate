"""Outbound adapters implementing the ports in ``permission_aware_retrieval.ports``."""

from permission_aware_retrieval.adapters.outbound.audit_sink import InMemoryAuditSink, JsonlAuditSink
from permission_aware_retrieval.adapters.outbound.event_bus import InMemoryEventBus
from permission_aware_retrieval.adapters.outbound.jsonl_repository import JsonlRunRepository
from permission_aware_retrieval.adapters.outbound.lexical_scorer import LexicalScorer
from permission_aware_retrieval.adapters.outbound.memory_corpus import InMemoryCorpus
from permission_aware_retrieval.adapters.outbound.memory_repository import InMemoryRunRepository
from permission_aware_retrieval.adapters.outbound.ttl_cache import TTLRankingCache

__all__ = [
    "InMemoryAuditSink",
    "InMemoryCorpus",
    "InMemoryEventBus",
    "InMemoryRunRepository",
    "JsonlAuditSink",
    "JsonlRunRepository",
    "LexicalScorer",
    "TTLRankingCache",
]
