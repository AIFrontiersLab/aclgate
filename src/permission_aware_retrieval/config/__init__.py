"""Typed configuration: defaults in code, profiles in TOML, overrides from the environment."""

from permission_aware_retrieval.config.loader import load_settings
from permission_aware_retrieval.config.settings import Settings

__all__ = ["Settings", "load_settings"]
