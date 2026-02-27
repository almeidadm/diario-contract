<!-- Copilot instructions for diario-contract repository -->
# Guia rápido para agentes de codificação (diario-contract)

Este repositório contém apenas definições de contrato (modelos Pydantic) usadas por toda a cadeia de ETL/RAG do projeto Diario. Objetivo: manter esquemas imutáveis e compatíveis retroativamente.

- **Arquitetura (visão geral)**
  - Pacote principal: `diario_contract/` — contém submódulos centrais: `article/`, `chunk/`, `embedding/`, `enums/`, `gazette/`, `parser/`, `rag/`, `retrieval/`.
  - Responsabilidade única: somente modelos e tipos (sem lógica de negócio). Outros serviços (ex.: `diario_crawler`, `diario_parser`, `diario_rag`) consomem estes contratos.

- **Princípios importantes (do README)**
  - Schemas são imutáveis; alterações devem preservar compatibilidade.
  - Versionamento via SemVer (veja `pyproject.toml` > `version`).
  - Pydantic v2 é obrigatório (`pyproject.toml` e `base.py`).

- **Padrões de implementação observados**
  - Todos os modelos herdam de `ContractModel` (`diario_contract/base.py`) com:

    - `frozen=True`, `extra='forbid'`, `validate_assignment=False` — ou seja, instâncias imutáveis e campos extras proibidos.
    - Exemplo de uso (teste): `Article(metadata=..., content=...)` (ver `tests/test_contract_models.py`).

  - Evitar campos mutáveis como defaults — usar `Field(default_factory=list)` para coleções (ex.: `GazetteEdition.articles` em `diario_contract/gazette/edition.py`).

  - Tipagem moderna: use `list[str]`, `str | None` (Python >= 3.10). Mantenha compatibilidade com `pyproject.toml` (>=3.10,<3.13).

- **Fluxos de desenvolvimento / comandos úteis**
  - Instalar pacote diretamente do repositório (conforme README):

    ```bash
    pip install git@github.com:almeidadm/diario-contract.git==1.*
    ```

  - Testes: `pytest` (dependência dev em `pyproject.toml`).

  - Versão do pacote: atualize apenas `pyproject.toml` [project]/version quando fizer mudanças compatíveis com SemVer; o runtime usa `importlib.metadata.version("diario-contract")` em `diario_contract/version.py`.

- **O que um agente deve evitar**
  - Não introduza lógica de negócio nos modelos — apenas tipos/validações.
  - Não modifique modelos existentes de forma breaking sem elevar major (`MAJOR` em SemVer).
  - Não permitir campos extras; se for necessário, siga o padrão `extra='forbid'` e documente mudanças.

- **Onde olhar para exemplos**
  - Organização de modelos: `diario_contract/article/`, `diario_contract/gazette/`, `diario_contract/chunk/`.
  - Configuração base: `diario_contract/base.py`.
  - Testes que exemplificam construção dos contratos: `tests/test_contract_models.py`.
  - Metadados do projeto: `pyproject.toml`, `README.md`.

Se alguma parte estiver incompleta ou você quiser incluir mais exemplos concretos (ex.: campos específicos de `ArticleContent` ou `EmbeddedChunk`), diga quais arquivos devo citar e eu atualizo o guia.
