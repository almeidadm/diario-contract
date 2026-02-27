from datetime import datetime

from diario_contract.base import ContractModel


class TextChunk(ContractModel):
    """Chunk de texto derivado de um artigo parseado."""

    chunk_id: str
    article_id: str
    edition_id: str
    order: int
    text: str
    tokens: int
    created_at: datetime
