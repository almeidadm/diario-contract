from __future__ import annotations

from datetime import date, datetime
from typing import Literal

from pydantic import Field, computed_field, field_validator, model_validator

from diario_contract.base import ContractModel
from diario_contract.enums.content_type import ContentType
from diario_contract.parser.named_entity import NamedEntityMention


class Act(ContractModel):
    """Canonical chunk/act emitted by parser and stored in silver/gold layers."""

    # identities
    chunk_id: str
    article_id: str
    edition_id: str
    city_id: str

    # publication context
    publication_date: date
    publication_month: str | None = None

    # gazette metadata (duplicated for preservation)
    edition_number: int | None = None
    supplement: bool | None = None
    edition_type_id: int | None = None
    edition_type_name: str | None = None
    pdf_url: str | None = None

    # article metadata (duplicated for preservation)
    title: str | None = None
    hierarchy_path: list[str] = Field(default_factory=list)
    identifier: str | None = None
    protocol: str | None = None
    section: str | None = None
    organization: str | None = None

    # content
    content_type: ContentType
    content_path: str
    text: str
    has_table: bool = False

    # chunking metadata
    chunk_i: int = 0
    chunk_strategy: str
    act_type: str | None = None
    is_actless: bool = False
    actless_reason: str | None = None
    start_offset: int = 0
    end_offset: int = 0

    # processing metadata
    processed_at: datetime
    batch_id: str | None = None
    parser_tag: str | None = None
    parse_status: Literal["ok", "warn", "fail"] | None = None
    quality_score: float | None = None

    # review metadata
    needs_review: bool = False
    review_status: Literal["pending", "approved", "rejected", "" ] | None = "pending"
    reviewer_id: str | None = None
    reviewed_at: datetime | None = None
    change_log: str | None = None

    # NER metadata
    entities: list[NamedEntityMention] = Field(default_factory=list)
    ner_model: str | None = None
    entity_catalog_version: int | None = None

    # gold tagging (optional on silver)
    embedding_model_tag: str | None = None
    retrieval_profile: str | None = None

    chunk_schema_version: int | None = None

    @computed_field
    @property
    def depth(self) -> int:
        return len(self.hierarchy_path)

    @field_validator("publication_month", mode="before")
    @classmethod
    def _compute_publication_month(cls, value: str | None):
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

    @model_validator(mode="after")
    def _sync_actless(self):  # type: ignore[override]
        if self.is_actless and not self.act_type:
            object.__setattr__(self, "act_type", "ACTLESS")
        if self.act_type == "ACTLESS" and not self.is_actless:
            object.__setattr__(self, "is_actless", True)
        return self

    @model_validator(mode="after")
    def _ensure_offsets(self):  # type: ignore[override]
        if self.start_offset < 0 or self.end_offset < 0:
            raise ValueError("Offsets must be non-negative")
        if self.end_offset and self.start_offset and self.end_offset < self.start_offset:
            raise ValueError("end_offset must be >= start_offset")
        return self

    def __repr__(self) -> str:  # pragma: no cover - cosmetic
        return f"<Act id={self.chunk_id} article={self.article_id} act_type={self.act_type}>"
