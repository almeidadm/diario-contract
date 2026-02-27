## Data Lifecycle

GazetteEdition
  ↓
Article
  ↓
ParsedArticle
  ↓
TextChunk
  ↓
EmbeddedChunk
  ↓
RetrievedDocument
  ↓
RAGAnswer

All lifecycle stages above have corresponding contracts in this repository.

Each stage:
- Consumes exactly one contract
- Produces exactly one contract
- Never mutates input objects
