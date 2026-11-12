"""Shared kernel: primitives every layer may depend on.

The kernel has no dependencies on any other package module. Domain, application,
adapters, and infrastructure all import from here, never the other way around.
"""

from permission_aware_retrieval.kernel.clock import Clock, FakeClock, SystemClock
from permission_aware_retrieval.kernel.errors import (
    ConfigurationError,
    DomainError,
    PolicyViolation,
    StageError,
    ValidationError,
)
from permission_aware_retrieval.kernel.result import Err, Ok, Result

__all__ = [
    "Clock",
    "ConfigurationError",
    "DomainError",
    "Err",
    "FakeClock",
    "Ok",
    "PolicyViolation",
    "Result",
    "StageError",
    "SystemClock",
    "ValidationError",
]
