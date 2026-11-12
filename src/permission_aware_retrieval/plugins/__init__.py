"""Extension points: stage factories and lifecycle hooks."""

from permission_aware_retrieval.plugins.hooks import HookManager
from permission_aware_retrieval.plugins.registry import StageRegistry

__all__ = ["HookManager", "StageRegistry"]
