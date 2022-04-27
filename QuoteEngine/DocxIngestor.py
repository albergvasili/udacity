"""Ingest Docx files."""
import docx
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """Inherit from IngestorInterface to convert and ingest docx files."""

    extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Verify if file is a docx, parse and return quotes."""
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest Exception')

        quotes = []
        doc = docx.Document(path)

        for x in doc.paragraphs:
            if x.text != "":
                parse = x.text.split('-')
                quote = QuoteModel(parse[0], parse[1])
                quotes.append(quote)

        return quotes
