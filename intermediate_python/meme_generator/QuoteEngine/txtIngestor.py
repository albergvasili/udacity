"""Ingest txt files."""

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List
import os


class txtIngestor(IngestorInterface):
    """Inherit from IngestorInterface to convert and ingest txt files."""

    extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Verify if file is a txt, parse and return quotes."""
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest Exception')

        quotes = []

        with open(path, 'r') as txt:
            for line in txt:
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parse = line.split('-')
                    quote = QuoteModel(parse[0], parse[1])
                    quotes.append(quote)

        return quotes
