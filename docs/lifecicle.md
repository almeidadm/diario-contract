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

Each stage:
- Consumes exactly one contract
- Produces exactly one contract
- Never mutates input objects
