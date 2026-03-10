from __future__ import annotations

from diario_contract.base import ContractModel


class NamedEntityMention(ContractModel):
    """Named entity span extracted from an Act/ParsedChunk."""

    entity_id: str | None = None
    text: str
    canonical_name: str | None = None
    label: str
    source_label: str | None = None
    start_char: int
    end_char: int
    source: str | None = None

    def __repr__(self) -> str:  # pragma: no cover - cosmetic
        return f"<NamedEntityMention label={self.label} text='{self.text}'>"
