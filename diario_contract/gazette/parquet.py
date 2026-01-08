import pyarrow as pa

EDITIONS_SCHEMA = pa.schema(
    [
        ("municipality", pa.string()),
        ("edition_id", pa.string()),
        ("publication_date", pa.date32()),
        ("edition_number", pa.int32()),
        ("supplement", pa.bool_()),
        ("edition_type_id", pa.int32()),
        ("edition_type_name", pa.string()),
        ("pdf_url", pa.string()),
        ("total_articles", pa.int32()),
        ("processed_at", pa.timestamp("us")),
        ("edition_hash", pa.string()),
        ("batch_id", pa.string()),
        ("year", pa.int32()),
        ("month", pa.int32()),
        ("day", pa.int32()),
    ]
)