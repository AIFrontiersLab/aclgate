# Permission Checker

Fail-closed tenant, clearance, and ACL filtering plus PII redaction.

| Property | Value |
|---|---|
| Stage | `permission_checker` |
| Role | `policy` |
| Interface | `process(ctx) -> None` |
| Critical | yes |
| Source | `src/permission_aware_retrieval/components/permission_checker/` |
| Tests | `tests/unit/components/test_component_permission_checker.py` |

## Behaviour

Fail-closed tenant, clearance, and ACL filtering plus PII redaction.

## Contract

- Input is bounded by `max_input_candidates`.
- Output contains no duplicate ids.
- Never introduces candidate ids that were not in its input.
- Ordering is preserved or intentionally changed per role.

## On failure

Run fails closed: no candidates survive, the run abstains with `policy_unavailable`.

## Metrics

- `component_permission_checker_runs_total`
- `component_permission_checker_candidates_out` (histogram)
- `component_permission_checker_removed_total`
