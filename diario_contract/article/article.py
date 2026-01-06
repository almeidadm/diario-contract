from diario_contract.article.metadata import ArticleMetadata
from diario_contract.article.content import ArticleContent, ContentType
from diario_contract.base import ContractModel


class Article(ContractModel):
    """Artigo completo com metadados e conteúdo."""

    metadata: ArticleMetadata
    content: ArticleContent

    @property
    def article_id(self) -> str:
        return self.metadata.article_id

    @property
    def title(self) -> str:
        return self.metadata.title

    @property
    def hierarchy_path(self) -> list[str]:
        return self.metadata.hierarchy_path

    @property
    def depth(self) -> int:
        return self.metadata.depth

    @property
    def raw_content(self) -> str | bytes:
        return self.content.raw_content

    @property
    def content_type(self) -> ContentType:
        return self.content.content_type

    def __repr__(self) -> str:
        return f"<Article id={self.article_id} title='{self.title}'>"