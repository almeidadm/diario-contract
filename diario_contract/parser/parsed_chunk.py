from datetime import date, datetime

from pydantic import Field

from diario_contract.base import ContractModel
from diario_contract.enums.content_type import ContentType


class NamedEntityMention(ContractModel):
    """Entidade reconhecida em um chunk parseado."""

    entity_id: str | None = None
    text: str
    canonical_name: str | None = None
    label: str
    source_label: str | None = None
    start_char: int
    end_char: int
    source: str


class ParsedChunk(ContractModel):
    """Chunk enriquecido produzido pelo parser antes de etapas downstream."""

    chunk_id: str
    identifier: str
    article_id: str | None = None
    edition_id: str
    municipality: str
    publication_date: date
    title: str | None = None
    section: str = ""
    organization: str = ""
    content_type: ContentType
    content_path: str
    chunk_i: int
    chunk_strategy: str
    act_type: str
    start_offset: int
    end_offset: int
    text: str
    has_table: bool = False
    processed_at: datetime | None = None
    batch_id: str | None = None
    entities: list[NamedEntityMention] = Field(default_factory=list)
    ner_model: str | None = None
    entity_catalog_version: int | None = None
