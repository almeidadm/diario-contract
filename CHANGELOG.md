# Changelog

All notable changes to this project are documented here.

## [2.0.0] - 2026-03-09

### Added
- New Act contract as canonical chunk with full Gazette/Article metadata and actless markers
- ActEmbedding contract for gold vectors aligned to storage `append_vectors`
- Parquet reference schemas for acts and vectors

### Changed
- ParsedChunk now mirrors Act fields (pre-storage)
- TextChunk/EmbeddedChunk aliased to Act/ActEmbedding for backward compatibility
- Package exports now include Act, ActEmbedding, parser, retrieval and RAG contracts; version bumped to 2.0.0

## [1.2.0] - 2026-03-06

### Added
- New parser-specific contracts: `ParsedChunk` and `NamedEntityMention`
- Support for chunk-level NER metadata in parser outputs

### Changed
- Exported parser-specific contracts from package namespaces
- Added local-checkout version fallback for uninstalled test environments

## [1.1.2] - 2026-02-26

### Changed
- Updated pyarrow dependency to 22.0.0

## [1.1.1] - 2026-02-26

### Added
- Lifecycle contracts: ParsedArticle, TextChunk, EmbeddedChunk, RetrievedDocument, RAGAnswer
- New retrieval and rag modules with exports
- Basic contract instantiation tests

### Changed
- Standardized Gazette publication_date to datetime.date in contracts
- Documented lifecycle contracts and date standardization

### Fixed
- GazetteEdition articles default now uses default_factory

## [1.1.0] - 2026-02-20

### Changed
Update README.md file

## [1.0.0] - 2026-01-05
### Added
- Initial stable data contract
- Gazette, Article
- Pydantic v2 base model
- Strict immutability and validation rules
