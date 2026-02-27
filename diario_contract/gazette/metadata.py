from datetime import date

from diario_contract.base import ContractModel

class GazetteMetadata(ContractModel):
    """Metadados de uma edição do diário."""

    edition_id: str
    publication_date: date
    edition_number: int
    supplement: bool
    edition_type_id: int
    edition_type_name: str
    pdf_url: str

    def __repr__(self) -> str:
        return f"<GazetteMetadata id={self.edition_id} date={self.publication_date}>"
