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
- TextChunk
- EmbeddedChunk
- RetrievedDocument
- RAGAnswer

Dates are standardized as `datetime.date` in contracts and stored as `date32` in Parquet.
