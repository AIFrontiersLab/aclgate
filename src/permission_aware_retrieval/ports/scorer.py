"""Relevance scoring port. Implementations must return values in [0, 1]."""

from __future__ import annotations

from typing import Protocol

from permission_aware_retrieval.domain.models import Candidate


class RelevanceScorer(Protocol):
    name: str

    def score(self, query: str, candidate: Candidate) -> float: ...
