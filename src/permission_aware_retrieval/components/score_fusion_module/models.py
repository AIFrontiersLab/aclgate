"""Value objects describing what Score Fusion Module did during one run."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field


@dataclass(frozen=True)
class ScoreFusionModuleInput:
    query: str
    candidate_ids: tuple[str, ...]

    @classmethod
    def from_context(cls, ctx) -> "ScoreFusionModuleInput":
        return cls(query=ctx.request.query, candidate_ids=tuple(c.doc_id for c in ctx.candidates))


@dataclass(frozen=True)
class ScoreFusionModuleReport:
    stage: str
    candidates_in: int
    candidates_out: int
    added: tuple[str, ...] = ()
    removed: tuple[str, ...] = ()
    notes: dict = field(default_factory=dict)

    @classmethod
    def diff(cls, stage: str, before: ScoreFusionModuleInput, after_ids: list[str], **notes) -> "ScoreFusionModuleReport":
        prior, now = set(before.candidate_ids), set(after_ids)
        return cls(
            stage=stage,
            candidates_in=len(before.candidate_ids),
            candidates_out=len(after_ids),
            added=tuple(sorted(now - prior)),
            removed=tuple(sorted(prior - now)),
            notes=dict(notes),
        )

    def to_dict(self) -> dict:
        out = asdict(self)
        out["added"] = list(self.added)
        out["removed"] = list(self.removed)
        return out
