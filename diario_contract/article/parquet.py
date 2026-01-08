import pyarrow as pa


ARTICLES_SCHEMA = pa.schema(
    [
        ("municipality", pa.string()),
        ("article_id", pa.string()),
        ("edition_id", pa.string()),
        ("edition_hash", pa.string()),
        ("publication_date", pa.date32()),
        ("title", pa.string()),
        ("hierarchy_path", pa.string()),  # JSON serializado
        ("identifier", pa.string()),
        ("protocol", pa.string()),
        ("depth", pa.int32()),
        ("content_type", pa.string()),
        ("content_size", pa.int64()),
        ("content_hash", pa.string()),
        ("content_path", pa.string()),
        ("inline_text", pa.string()),
        ("processed_at", pa.timestamp("us")),
        ("batch_id", pa.string()),
        ("year", pa.int32()),
        ("month", pa.int32()),
        ("day", pa.int32()),
    ]
)