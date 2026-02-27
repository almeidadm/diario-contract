# Changelog

All notable changes to this project are documented here.

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
