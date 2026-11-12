# Getting started

1. `python -m venv .venv && source .venv/bin/activate`
2. `pip install -e ".[dev]"`
3. `make test`
4. `python -m permission_aware_retrieval run examples/requests/governed_query.json`
5. `python -m permission_aware_retrieval serve` and `curl -s localhost:8080/v1/pipeline`
