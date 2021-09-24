"""Create a base class for ingesting files."""


from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface():
    """Base ingestor class.

    This contains class methods and does not need to be
    instantiated. It encapsulates our import functionality
    and can be called to load different file types.
    """

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path):
        """Check that the file extension is in the allow list."""
        return path.split('.')[-1] in cls.allowed_extensions

    @abstractmethod
    @classmethod
    def parse_quotes(cls, path: str) -> List(QuoteModel):
        """Extract quotations line by line from the document."""
        pass
