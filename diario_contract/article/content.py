from diario_contract.base import ContractModel
from diario_contract.enums.content_type import ContentType


class ArticleContent(ContractModel):
    """Conteúdo processado de um artigo."""

    raw_content: str | bytes
    content_type: ContentType

    def __repr__(self) -> str:
        return f"<ArticleContent type={self.content_type} size={len(self.raw_content)}>"

