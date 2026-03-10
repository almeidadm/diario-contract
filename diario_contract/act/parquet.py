import pyarrow as pa

ACT_SCHEMA = pa.schema(
    [
        ("city_id", pa.string()),
        ("publication_month", pa.string()),
        ("parser_tag", pa.string()),
        ("chunk_id", pa.string()),
        ("article_id", pa.string()),
        ("edition_id", pa.string()),
        ("edition_number", pa.int32()),
        ("supplement", pa.bool_()),
        ("edition_type_id", pa.int32()),
        ("edition_type_name", pa.string()),
        ("pdf_url", pa.string()),
        ("publication_date", pa.date32()),
        ("title", pa.string()),
        ("hierarchy_path", pa.string()),  # JSON serialized
        ("identifier", pa.string()),
        ("protocol", pa.string()),
        ("section", pa.string()),
        ("organization", pa.string()),
        ("content_type", pa.string()),
        ("content_path", pa.string()),
        ("chunk_i", pa.int32()),
        ("chunk_strategy", pa.string()),
        ("act_type", pa.string()),
        ("is_actless", pa.bool_()),
        ("actless_reason", pa.string()),
        ("start_offset", pa.int32()),
        ("end_offset", pa.int32()),
        ("text", pa.string()),
        ("has_table", pa.bool_()),
        ("processed_at", pa.timestamp("us")),
        ("batch_id", pa.string()),
        ("parse_status", pa.string()),
        ("quality_score", pa.float64()),
        ("needs_review", pa.bool_()),
        ("review_status", pa.string()),
        ("reviewer_id", pa.string()),
        ("reviewed_at", pa.timestamp("us")),
        ("change_log", pa.string()),
        ("entities", pa.string()),  # JSON serialized list
        ("ner_model", pa.string()),
        ("entity_catalog_version", pa.int32()),
        ("embedding_model_tag", pa.string()),
        ("retrieval_profile", pa.string()),
        ("chunk_schema_version", pa.int32()),
    ]
)

VECTORS_SCHEMA = pa.schema(
    [
        ("chunk_id", pa.string()),
        ("article_id", pa.string()),
        ("edition_id", pa.string()),
        ("city_id", pa.string()),
        ("publication_date", pa.date32()),
        ("publication_month", pa.string()),
        ("embedding", pa.list_(pa.float32())),
        ("embedding_model_tag", pa.string()),
        ("retrieval_profile", pa.string()),
        ("created_at", pa.timestamp("us")),
    ]
)
"""Reference schemas for Acts and embeddings when writing Parquet."""
