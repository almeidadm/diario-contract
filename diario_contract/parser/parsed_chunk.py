from __future__ import annotations

from datetime import date, datetime
from typing import Literal

from pydantic import Field, field_validator, model_validator

from diario_contract.base import ContractModel
from diario_contract.enums.content_type import ContentType
from diario_contract.parser.named_entity import NamedEntityMention


class ParsedChunk(ContractModel):
    """Parser output before storage; mirrors Act minus review/embedding tags."""

    chunk_id: str
    identifier: str
    article_id: str
    edition_id: str
    municipality: str | None = None
    city_id: str | None = None

    publication_date: date
    publication_month: str | None = None

    title: str | None = None
    section: str | None = None
    organization: str | None = None
    content_type: ContentType
    content_path: str

    chunk_i: int = 0
    chunk_strategy: str
    act_type: str
    start_offset: int = 0
    end_offset: int = 0
    text: str
    has_table: bool = False

    processed_at: datetime | None = None
    batch_id: str | None = None

    entities: list[NamedEntityMention] = Field(default_factory=list)
    ner_model: str | None = None
    entity_catalog_version: int | None = None

    parser_tag: str | None = None
    parse_status: Literal["ok", "warn", "fail"] | None = None
    quality_score: float | None = None
    needs_review: bool = False

    @field_validator("publication_month", mode="before")
    @classmethod
    def _keep_publication_month(cls, value: str | None):
        return value

    @model_validator(mode="after")
    def _compute_publication_month(self):  # type: ignore[override]
        if not self.publication_month and isinstance(self.publication_date, date):
            object.__setattr__(
                self,
                "publication_month",
                f"{self.publication_date.year:04d}{self.publication_date.month:02d}",
            )
        return self

    @model_validator(mode="after")
    def _sync_city(self):  # type: ignore[override]
        if self.city_id is None and self.municipality is not None:
            object.__setattr__(self, "city_id", self.municipality)
        return self

    def __repr__(self) -> str:  # pragma: no cover - cosmetic
        return f"<ParsedChunk id={self.chunk_id} article={self.article_id} strategy={self.chunk_strategy}>"
