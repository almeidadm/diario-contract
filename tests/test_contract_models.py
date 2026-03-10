from datetime import date, datetime

from diario_contract import (
    Act,
    ActEmbedding,
    NamedEntityMention,
    ParsedArticle,
    ParsedChunk,
    RAGAnswer,
    RetrievedDocument,
)
from diario_contract.article.article import Article
from diario_contract.article.content import ArticleContent
from diario_contract.article.metadata import ArticleMetadata
from diario_contract.enums.content_type import ContentType
from diario_contract.gazette.edition import GazetteEdition
from diario_contract.gazette.metadata import GazetteMetadata


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


def test_act_and_embedding_instantiate_with_actless():
    now = datetime(2024, 1, 1, 12, 0, 0)
    mention = NamedEntityMention(
        entity_id="org-prefeitura-sjc",
        text="Prefeitura Municipal",
        canonical_name="Prefeitura Municipal de Sao Jose dos Campos",
        label="ORG",
        source_label="ORG",
        start_char=0,
        end_char=21,
        source="spacy+catalog",
    )

    act = Act(
        chunk_id="chunk-1",
        article_id="a-1",
        edition_id="ed-1",
        city_id="sp_sao_jose_dos_campos",
        publication_date=date(2024, 1, 1),
        title="Titulo",
        hierarchy_path=["A", "B"],
        identifier="ID-1",
        protocol=None,
        section="Secao",
        organization="Orgao",
        content_type=ContentType.TEXT,
        content_path="raw/path",
        chunk_i=0,
        chunk_strategy="regex_v2",
        act_type="ACTLESS",
        is_actless=True,
        start_offset=0,
        end_offset=10,
        text="texto",
        has_table=False,
        processed_at=now,
        batch_id="batch-1",
        entities=[mention],
        ner_model="pt_core_news_lg",
        entity_catalog_version=1,
        parser_tag="v1",
        needs_review=True,
        review_status="pending",
    )

    assert act.publication_month == "202401"
    assert act.is_actless is True
    assert act.act_type == "ACTLESS"
    assert act.depth == 2
    assert act.entities and act.entities[0].label == "ORG"

    embedding = ActEmbedding(
        chunk_id=act.chunk_id,
        article_id=act.article_id,
        edition_id=act.edition_id,
        city_id=act.city_id,
        publication_date=act.publication_date,
        embedding=[0.1, 0.2, 0.3],
        embedding_model_tag="model-v1",
        retrieval_profile="default",
        created_at=now,
    )

    assert embedding.publication_month == "202401"
    assert embedding.embedding_model_tag == "model-v1"


def test_parser_and_rag_contracts_instantiate():
    now = datetime(2024, 2, 1, 9, 30, 0)
    article = ParsedArticle(
        article_id="a-1",
        edition_id="ed-1",
        title="Titulo",
        hierarchy_path=["A", "B"],
        content_type=ContentType.TEXT,
        parsed_text="texto",
        parsed_at=now,
    )
    assert article.parsed_at == now

    parsed_chunk = ParsedChunk(
        chunk_id="chunk-1",
        identifier="ID-1",
        article_id="a-1",
        edition_id="ed-1",
        municipality="sp_sao_jose_dos_campos",
        publication_date=date(2024, 1, 1),
        title="Titulo",
        section="Secao",
        organization="Orgao",
        content_type=ContentType.TEXT,
        content_path="raw/path",
        chunk_i=0,
        chunk_strategy="regex_v2",
        act_type="LEI",
        start_offset=0,
        end_offset=10,
        text="texto",
        has_table=False,
        processed_at=now,
        batch_id="batch-1",
        entities=[],
        ner_model="pt_core_news_lg",
        entity_catalog_version=1,
        parser_tag="v1",
        needs_review=False,
    )
    assert parsed_chunk.publication_month == "202401"
    assert parsed_chunk.city_id == "sp_sao_jose_dos_campos"

    retrieved = RetrievedDocument(
        query_id="q-1",
        chunk_id="chunk-1",
        score=0.95,
        rank=1,
        retrieved_at=now,
    )
    assert retrieved.score == 0.95

    answer = RAGAnswer(
        query_id="q-1",
        answer="resposta",
        sources=["chunk-1"],
        generated_at=now,
    )
    assert answer.sources == ["chunk-1"]


def test_article_contracts_remain_unchanged():
    article_metadata = ArticleMetadata(
        article_id="a-1",
        edition_id="ed-1",
        hierarchy_path=["A", "B"],
        title="Titulo",
        identifier="ID-1",
        protocol=None,
    )
    content = ArticleContent(raw_content="conteudo", content_type=ContentType.TEXT)
    article = Article(metadata=article_metadata, content=content)

    assert article.article_id == "a-1"
    assert article.title == "Titulo"
    assert article.depth == 2
