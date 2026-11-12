# Request sequence

```mermaid
sequenceDiagram
    autonumber
    participant C as Client
    participant H as HTTP adapter
    participant B as Message bus
    participant O as Orchestrator
    participant S as Stages
    participant R as Run repository
    C->>H: POST /v1/runs
    H->>H: request id, rate limit, parse
    H->>B: RunPipeline
    B->>O: execute(request)
    O->>O: bulkhead slot, RUNNING
    O->>S: intake (breaker + retry + span)
    O->>S: corpus_retrieval (breaker + retry + span)
    O->>S: signal_enricher (breaker + retry + span)
    O->>S: ranking_cache (breaker + retry + span)
    O->>S: hybrid_retrieval_engine (breaker + retry + span)
    O->>S: score_fusion_module (breaker + retry + span)
    O->>S: graceful_fallback (breaker + retry + span)
    O->>S: permission_checker (breaker + retry + span)
    O->>S: token_budget_governor (breaker + retry + span)
    O->>S: answer_assembly (breaker + retry + span)
    S-->>O: context mutated
    O->>O: COMPLETED / ABSTAINED / AWAITING_APPROVAL
    O-->>B: Outcome
    B->>R: commit RunRecord (unit of work)
    B-->>H: outcome dict
    H-->>C: 200 / 202 with envelope
```
