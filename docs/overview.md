## What is a Data Contract?

A data contract defines:
- Field names
- Field types
- Ownership
- Evolution rules

This repository is the ONLY place where schemas may be defined.
Downstream repositories MUST import models from here.

## Lifecycle Contracts

The lifecycle contracts currently defined include:
- GazetteEdition
- Article
- ParsedArticle
- ParsedChunk
- Act (canonical chunk)
- ActEmbedding
- RetrievedDocument
- RAGAnswer

Dates are standardized as `datetime.date` in contracts and stored as `date32` in Parquet.

Act specifics:
- Acts duplicate Gazette + Article metadata so each chunk is self-sufficient.
- When no act is detected or acts are too long, set `is_actless=true` and `act_type="ACTLESS"` while keeping `chunk_strategy` to describe the fallback.
- ActEmbedding aligns with storage gold vectors (`embedding_model_tag`, `retrieval_profile`).
