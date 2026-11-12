"""Signal Enricher.

Annotates candidates with token counts and query overlap, and collapses duplicate passages.
"""

from permission_aware_retrieval.components.signal_enricher.adapter import ROLE, build
from permission_aware_retrieval.components.signal_enricher.config import CONFIG, SignalEnricherConfig
from permission_aware_retrieval.components.signal_enricher.errors import SignalEnricherError
from permission_aware_retrieval.components.signal_enricher.service import SignalEnricherService

__all__ = ["CONFIG", "ROLE", "build", "SignalEnricherConfig", "SignalEnricherError", "SignalEnricherService"]
