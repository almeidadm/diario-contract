from diario_contract.base import ContractModel

class ArticleMetadata(ContractModel):
    """Metadados de um artigo."""

    article_id: str
    edition_id: str
    hierarchy_path: list[str]
    title: str
    identifier: str
    protocol: str | None = None

    @property
    def depth(self) -> int:
        return len(self.hierarchy_path)

    def __repr__(self) -> str:
        return f"<ArticleMetadata id={self.article_id} title='{self.title}'>"