"""Observability: structured logs, trace spans, metrics, health checks."""

from permission_aware_retrieval.observability.health import HealthRegistry
from permission_aware_retrieval.observability.logging import get_logger
from permission_aware_retrieval.observability.metrics import MetricsRegistry
from permission_aware_retrieval.observability.tracing import Tracer

__all__ = ["HealthRegistry", "MetricsRegistry", "Tracer", "get_logger"]
