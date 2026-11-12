"""Permission-Aware Retrieval: governed reference service.

Enforce document access before context assembly.

Public entry points:

* ``build_container`` - wire the full object graph from settings.
* ``run`` - execute a single request and return the outcome as a dict.
"""

from permission_aware_retrieval.application.pipeline import run
from permission_aware_retrieval.container import build_container
from permission_aware_retrieval.version import __version__

__all__ = ["__version__", "build_container", "run"]
