# Score Fusion Module

Blends upstream prior scores with query-aware relevance and reorders candidates.

| Property | Value |
|---|---|
| Stage name | `score_fusion_module` |
| Role | `score` |
| Interface | `process(ctx) -> None` |
| Critical | No. A failure degrades the run and downstream fallback restores a safe ordering. |
| Origin | architecture specification |

## Files

| File | Purpose |
|---|---|
| `config.py` | Frozen configuration dataclass and defaults |
| `service.py` | `ScoreFusionModuleService` (role strategy plus contract checks) and metric recording |
| `validators.py` | Pre/post conditions (bounded input, no duplicate or unknown ids, ordering) |
| `models.py` | Input snapshot and per-run report |
| `errors.py` | Component error types (all `StageError` subclasses) |
| `adapter.py` | Port protocol and the factory registered in the stage registry |

## Behaviour

Blends upstream prior scores with query-aware relevance and reorders candidates.

See also [`docs/components/score_fusion_module.md`](../../../../docs/components/score_fusion_module.md).
