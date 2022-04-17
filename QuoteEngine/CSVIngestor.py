"""Ingest CSV files using pandas library."""

import csv
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

        with open(path, 'r') as infile:
            reader = csv.DictReader(infile)

            for elem in reader:
                quote = QuoteModel(elem['body'], elem['author'])
                quotes.append(quote)

        #I'm having an error related to the numpy dependency, so I decided
        #to import the csv library instead.

        #df = pandas.read_csv(path, header=0)
        #for index, row in df.iterrows():
            #quote = QuoteModel(row['body'], row['author'])
            #quotes.append(quote)

        return quotes
