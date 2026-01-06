from pydantic import Field

from diario_contract.base import ContractModel
from diario_contract.gazette.metadata import GazetteMetadata
from diario_contract.article.article import Article

class GazetteEdition(ContractModel):
    """Edição completa do diário com seus artigos."""

    metadata: GazetteMetadata
    articles: list[Article] = []

    @property
    def edition_id(self) -> str:
        return self.metadata.edition_id

    @property
    def publication_date(self) -> str:
        return self.metadata.publication_date

    @property
    def total_articles(self) -> int:
        return len(self.articles)

    def __repr__(self) -> str:
        return (
            f"<GazetteEdition id={self.edition_id} "
            f"date={self.publication_date} "
            f"articles={self.total_articles}>"
        )