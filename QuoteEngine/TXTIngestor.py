"""Callable IngestorInterface subclass that parses txt files."""


from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List


class TXTIngestor(IngestorInterface):
    """Import and parse txt files into QuoteModel objects."""

    allowed_extensions = ['txt']

    @classmethod
    def parse_quotes(cls, path: str) -> List[QuoteModel]:
        """Parse the txt file into a list of QuoteModel objects.

        Each line from the file should be a new quote, and the
        function will split out the author and body.
        """
        if not cls.can_ingest(path):
            raise Exception('incompatible file type')

        quotes = []

        with open(path, 'r') as infile:
            doc = infile.read()

        for row in doc.split('\n'):
            body, author = row.split('-')
            quote = QuoteModel(author=author.strip(), body=body.strip())
            quotes.append(quote)

        return quotes
