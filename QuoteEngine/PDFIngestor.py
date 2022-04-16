from .IngestorInterface import IngestorInterface
from .QuoteModule import QuoteModule
from typing import List
import os
import subprocess


class PDFIngestor(IngestorInterface):
    extensions = ['.pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModule]:
        if not cls.can_ingest(path):
            raise Exception("Cannot ingest Exception")

        quotes = []
        new_file = f'{path.split(".")[0]}.txt'
        subprocess.call(['pdftotext', path, new_file])

        with open(new_file, 'r') as new:
            for line in new.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parse = line.split('-')
                    quote = QuoteModel(parse[0], parse[1])
                    quotes.append(quote)

        os.remove(new_file)
        return quotes
