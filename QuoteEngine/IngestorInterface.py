"""Abstract base class to be used by helper ingestor classes."""

from .QuoteModule import QuoteModule
from typing import List
from abc import ABC, abstractmethod


class IngestorInterface(ABC):
    """Provide layout for ingestors."""

    extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Verify if file type is compatible"""
        ext = path.split('.')[-1]
        return ext in extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModule}:
        """Abstract method for parsing file content"""
        pass
