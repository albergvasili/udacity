"""Ingest CSV files using pandas library."""

import pandas
from .IngestorInterface import IngestorInterface
from typing import List


class CSVIngestor(IngestorInterface):
    """Inherit from IngestorInterface to read and ingest CSV files."""

    extensions = ['.csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Verify if file is a csv, parse and return quote."""

        if not cls.can_ingest(path):
            raise Exception('Cannot ingest Exception')

        quotes = []

        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            quote = QuoteModel(row['body'], row['author'])
            quotes.append(quote)

        return quotes
