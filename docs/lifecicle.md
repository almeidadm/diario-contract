## Data Lifecycle

GazetteEdition
  ↓
Article
  ↓
ParsedArticle
  ↓
ParsedChunk
  ↓
Act (silver/gold)
  ↓
ActEmbedding (gold vectors)
  ↓
RetrievedDocument
  ↓
RAGAnswer

All lifecycle stages above have corresponding contracts in this repository.

Each stage:
- Consumes exactly one contract
- Produces exactly one contract
- Never mutates input objects
