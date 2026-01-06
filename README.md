# Diario Data Contract

Authoritative schema definitions for the Diario RAG ETL pipeline.

This repository defines all data exchanged between:
- diario_crawler
- diario_normalizer
- diario_parser
- diario_chunker
- diario_embedding
- diario_retrieval
- diario_rag
- diario_rag_ui

## Principles

- Schemas are immutable
- Backward compatibility is enforced
- No business logic
- Versioned via SemVer
- Pydantic v2 only

## Installation

pip install git@github.com:almeidadm/diario-contract.git==1.*

## Contract Version

Current: 1.0.0
