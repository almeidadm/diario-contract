from __future__ import annotations

from datetime import datetime

from diario_contract.base import ContractModel


class RAGAnswer(ContractModel):
    """Final RAG answer with source references."""

    query_id: str
    answer: str
    sources: list[str]
    generated_at: datetime

    def __repr__(self) -> str:  # pragma: no cover - cosmetic
        return f"<RAGAnswer query={self.query_id} sources={len(self.sources)}>"
