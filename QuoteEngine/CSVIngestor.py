import pandas
from .IngestorInterface import IngestorInterface
from typing import List


class CSVIngestor(IngestorInterface):
    extensions = ['.csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest Exception')

        quotes = []

        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            quote = QuoteModel(row['body'], row['author'])
            quotes.append(quote)

        return quotes
