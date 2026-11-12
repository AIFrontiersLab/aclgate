# Components (C4 level 3)

| # | Stage | Role | Critical | Source |
|---|---|---|---|---|
| 1 | `intake` (Intake) | `ingest` | yes | built-in |
| 2 | `corpus_retrieval` (Corpus Retrieval) | `retrieve` | no | built-in |
| 3 | `signal_enricher` (Signal Enricher) | `enrich` | no | [component](../components/signal_enricher.md) |
| 4 | `ranking_cache` (Ranking Cache) | `cache` | no | [component](../components/ranking_cache.md) |
| 5 | `hybrid_retrieval_engine` (Hybrid Retrieval Engine) | `score` | no | [component](../components/hybrid_retrieval_engine.md) |
| 6 | `score_fusion_module` (Score Fusion Module) | `score` | no | [component](../components/score_fusion_module.md) |
| 7 | `graceful_fallback` (Graceful Fallback) | `fallback` | no | built-in |
| 8 | `permission_checker` (Permission Checker) | `policy` | yes | [component](../components/permission_checker.md) |
| 9 | `token_budget_governor` (Token Budget Governor) | `budget` | no | [component](../components/token_budget_governor.md) |
| 10 | `answer_assembly` (Answer Assembly) | `answer` | yes | built-in |

Each concept component follows the same internal layout so reviewers can navigate
any of them blind: `config.py`, `port.py`, `service.py`, `validators.py`, `models.py`,
`metrics.py`, `errors.py`, `adapter.py`.
