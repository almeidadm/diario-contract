from datetime import date, datetime

from diario_contract.article.content import ArticleContent
from diario_contract.article.metadata import ArticleMetadata
from diario_contract.article.article import Article
from diario_contract.chunk.text_chunk import TextChunk
from diario_contract.embedding.embedded_chunk import EmbeddedChunk
from diario_contract.enums.content_type import ContentType
from diario_contract.gazette.edition import GazetteEdition
from diario_contract.gazette.metadata import GazetteMetadata
from diario_contract.parser.parsed_article import ParsedArticle
from diario_contract.rag.answer import RAGAnswer
from diario_contract.retrieval.retrieved_document import RetrievedDocument


def _metadata():
    return GazetteMetadata(
        edition_id="ed-1",
        publication_date=date(2024, 1, 1),
        edition_number=1,
        supplement=False,
        edition_type_id=1,
        edition_type_name="Ordinaria",
        pdf_url="https://example.com/ed-1.pdf",
    )


def test_gazette_articles_default_factory():
    g1 = GazetteEdition(metadata=_metadata())
    g2 = GazetteEdition(metadata=_metadata())
    assert g1.articles == []
    assert g1.articles is not g2.articles


def test_publication_date_is_date():
    metadata = _metadata()
    assert isinstance(metadata.publication_date, date)


def test_lifecycle_contracts_instantiate():
    now = datetime(2024, 1, 1, 12, 0, 0)
    article_metadata = ArticleMetadata(
        article_id="a-1",
        edition_id="ed-1",
        hierarchy_path=["A", "B"],
        title="Titulo",
        identifier="ID-1",
        protocol=None,
    )
    content = ArticleContent(raw_content="conteudo", content_type=ContentType.TEXT)
    Article(metadata=article_metadata, content=content)

    ParsedArticle(
        article_id="a-1",
        edition_id="ed-1",
        title="Titulo",
        hierarchy_path=["A", "B"],
        content_type=ContentType.TEXT,
        parsed_text="texto",
        parsed_at=now,
    )
    TextChunk(
        chunk_id="c-1",
        article_id="a-1",
        edition_id="ed-1",
        order=0,
        text="texto",
        tokens=10,
        created_at=now,
    )
    EmbeddedChunk(
        chunk_id="c-1",
        article_id="a-1",
        embedding=[0.1, 0.2, 0.3],
        embedding_model="model-v1",
        created_at=now,
    )
    RetrievedDocument(
        query_id="q-1",
        chunk_id="c-1",
        score=0.95,
        rank=1,
        retrieved_at=now,
    )
    RAGAnswer(
        query_id="q-1",
        answer="resposta",
        sources=["c-1"],
        generated_at=now,
    )
