# Permission Checker

Fail-closed tenant, clearance, and ACL filtering plus PII redaction.

| Property | Value |
|---|---|
| Stage name | `permission_checker` |
| Role | `policy` |
| Interface | `process(ctx) -> None` |
| Critical | Yes. A failure stops the run and fails closed. |
| Origin | architecture specification |

## Files

| File | Purpose |
|---|---|
| `config.py` | Frozen configuration dataclass and defaults |
| `service.py` | `PermissionCheckerService` (role strategy plus contract checks) and metric recording |
| `validators.py` | Pre/post conditions (bounded input, no duplicate or unknown ids, ordering) |
| `models.py` | Input snapshot and per-run report |
| `errors.py` | Component error types (all `StageError` subclasses) |
| `adapter.py` | Port protocol and the factory registered in the stage registry |

## Behaviour

Fail-closed tenant, clearance, and ACL filtering plus PII redaction.

See also [`docs/components/permission_checker.md`](../../../../docs/components/permission_checker.md).
