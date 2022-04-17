"""Abstract base class to be used by helper ingestor classes."""

from .QuoteModel import QuoteModel
from typing import List
from abc import ABC, abstractmethod


class IngestorInterface(ABC):
    """Provide layout for ingestors."""

    extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Verify if file type is compatible"""
        ext = path.split('.')[-1]
        return ext in cls.extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Abstract method for parsing file content"""
        pass
