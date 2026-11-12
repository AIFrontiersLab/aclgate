"""Token Budget Governor.

Enforces per-request and global token ceilings before evidence reaches the answer stage.
"""

from permission_aware_retrieval.components.token_budget_governor.adapter import ROLE, build
from permission_aware_retrieval.components.token_budget_governor.config import CONFIG, TokenBudgetGovernorConfig
from permission_aware_retrieval.components.token_budget_governor.errors import TokenBudgetGovernorError
from permission_aware_retrieval.components.token_budget_governor.service import TokenBudgetGovernorService

__all__ = ["CONFIG", "ROLE", "build", "TokenBudgetGovernorConfig", "TokenBudgetGovernorError", "TokenBudgetGovernorService"]
