# Score Fusion Module

Blends upstream prior scores with query-aware relevance and reorders candidates.

| Property | Value |
|---|---|
| Stage | `score_fusion_module` |
| Role | `score` |
| Interface | `process(ctx) -> None` |
| Critical | no |
| Source | `src/permission_aware_retrieval/components/score_fusion_module/` |
| Tests | `tests/unit/components/test_component_score_fusion_module.py` |

## Behaviour

Blends upstream prior scores with query-aware relevance and reorders candidates.

## Contract

- Input is bounded by `max_input_candidates`.
- Output contains no duplicate ids.
- Never introduces candidate ids that were not in its input.
- Output is sorted by descending score.

## On failure

Run degrades; fallback restores upstream prior order.

## Metrics

- `component_score_fusion_module_runs_total`
- `component_score_fusion_module_candidates_out` (histogram)
- `component_score_fusion_module_removed_total`
