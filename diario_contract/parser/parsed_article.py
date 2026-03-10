from __future__ import annotations

from datetime import datetime

from diario_contract.base import ContractModel
from diario_contract.enums.content_type import ContentType


class ParsedArticle(ContractModel):
    """Article parsed and ready for chunking."""

    article_id: str
    edition_id: str
    title: str
    hierarchy_path: list[str]
    content_type: ContentType
    parsed_text: str
    parsed_at: datetime

    def __repr__(self) -> str:  # pragma: no cover - cosmetic
        return f"<ParsedArticle id={self.article_id} title='{self.title}'>"
