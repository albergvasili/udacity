"""This class encapsulates the other ingestor classes."""

from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from .CSVIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor
from .txtIngestor import txtIngestor


class Ingestor(IngestorInterface):
    """Choose appropriate ingestor class to process path file."""

    ingestors = [CSVIngestor, DocxIngestor, PDFIngestor, txtIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Check extension and parse file to return quote."""
        for ingest in cls.ingestors:
            if ingest.can_ingest(path):
                return ingest.parse(path)
