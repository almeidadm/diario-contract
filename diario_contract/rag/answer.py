from datetime import datetime

from diario_contract.base import ContractModel


class RAGAnswer(ContractModel):
    """Resposta final com referências às fontes."""

    query_id: str
    answer: str
    sources: list[str]
    generated_at: datetime
