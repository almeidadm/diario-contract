from __future__ import annotations

from datetime import date, datetime

from pydantic import field_validator, model_validator

from diario_contract.base import ContractModel


class ActEmbedding(ContractModel):
    """Embedding vector associated with an Act (gold layer)."""

    chunk_id: str
    article_id: str | None = None
    edition_id: str | None = None
    city_id: str

    publication_date: date
    publication_month: str | None = None

    embedding: list[float]
    embedding_model_tag: str
    retrieval_profile: str
    created_at: datetime

    @field_validator("publication_month", mode="before")
    @classmethod
    def _keep_publication_month(cls, value: str | None):
        return value

    @model_validator(mode="after")
    def _ensure_publication_month(self):  # type: ignore[override]
        if not self.publication_month and isinstance(self.publication_date, date):
            object.__setattr__(
                self,
                "publication_month",
                f"{self.publication_date.year:04d}{self.publication_date.month:02d}",
            )
        return self

    def __repr__(self) -> str:  # pragma: no cover - cosmetic
        return f"<ActEmbedding chunk={self.chunk_id} model={self.embedding_model_tag}>"
