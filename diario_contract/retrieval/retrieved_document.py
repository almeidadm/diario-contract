from datetime import datetime

from diario_contract.base import ContractModel


class RetrievedDocument(ContractModel):
    """Documento recuperado para um contexto de busca."""

    query_id: str
    chunk_id: str
    score: float
    rank: int
    retrieved_at: datetime
