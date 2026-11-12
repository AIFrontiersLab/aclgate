#!/usr/bin/env bash
set -euo pipefail
export PERMISSION_AWARE_RETRIEVAL_CONFIG=${PERMISSION_AWARE_RETRIEVAL_CONFIG:-config/development.toml}
PYTHONPATH=src exec python -m permission_aware_retrieval serve "$@"
