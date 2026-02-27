from datetime import datetime

from diario_contract.base import ContractModel


class EmbeddedChunk(ContractModel):
    """Chunk com embedding associado."""

    chunk_id: str
    article_id: str
    embedding: list[float]
    embedding_model: str
    created_at: datetime
