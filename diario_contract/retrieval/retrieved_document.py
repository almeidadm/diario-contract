from __future__ import annotations

from datetime import datetime

from diario_contract.base import ContractModel


class RetrievedDocument(ContractModel):
    """Document retrieved for a query context."""

    query_id: str
    chunk_id: str
    score: float
    rank: int
    retrieved_at: datetime

    def __repr__(self) -> str:  # pragma: no cover - cosmetic
        return f"<RetrievedDocument chunk={self.chunk_id} score={self.score}>"
