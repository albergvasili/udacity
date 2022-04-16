from .QuoteModule import QuoteModule
from typing import List
from abc import ABC, abstractmethod


class IngestorInterface(ABC):
    extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        ext = path.split('.')[-1]
        return ext in extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModule}:
        pass
