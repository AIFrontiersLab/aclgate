"""Permission Checker.

Fail-closed tenant, clearance, and ACL filtering plus PII redaction.
"""

from permission_aware_retrieval.components.permission_checker.adapter import ROLE, build
from permission_aware_retrieval.components.permission_checker.config import CONFIG, PermissionCheckerConfig
from permission_aware_retrieval.components.permission_checker.errors import PermissionCheckerError
from permission_aware_retrieval.components.permission_checker.service import PermissionCheckerService

__all__ = ["CONFIG", "ROLE", "build", "PermissionCheckerConfig", "PermissionCheckerError", "PermissionCheckerService"]
