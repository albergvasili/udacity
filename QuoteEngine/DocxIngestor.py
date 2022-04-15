import docx
from typing import List
from .Ingestor import IngestorInterface


class DocxIngestor(IngestorInterface):
    extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest Exception')

        quotes = []
        doc = docx.Document(path)

        for x in doc.paragraphs:
            if x.text != "":
                parse = para.text.split('-')
                quote = QuoteModel(parse[0], parse[1])
                quotes.append(quote)

        return quotes
