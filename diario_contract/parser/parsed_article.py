from datetime import datetime

from diario_contract.base import ContractModel
from diario_contract.enums.content_type import ContentType


class ParsedArticle(ContractModel):
    """Artigo parseado pronto para chunking."""

    article_id: str
    edition_id: str
    title: str
    hierarchy_path: list[str]
    content_type: ContentType
    parsed_text: str
    parsed_at: datetime
