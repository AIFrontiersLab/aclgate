"""Score Fusion Module.

Blends upstream prior scores with query-aware relevance and reorders candidates.
"""

from permission_aware_retrieval.components.score_fusion_module.adapter import ROLE, build
from permission_aware_retrieval.components.score_fusion_module.config import CONFIG, ScoreFusionModuleConfig
from permission_aware_retrieval.components.score_fusion_module.errors import ScoreFusionModuleError
from permission_aware_retrieval.components.score_fusion_module.service import ScoreFusionModuleService

__all__ = ["CONFIG", "ROLE", "build", "ScoreFusionModuleConfig", "ScoreFusionModuleError", "ScoreFusionModuleService"]
