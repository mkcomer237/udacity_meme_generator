"""Callable IngestorInterface subclass that parses csv files."""


from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List
import pandas


class CSVIngestor(IngestorInterface):
    """Import and parse csv files into QuoteModel objects."""

    allowed_extensions = ['csv']

    @classmethod
    def parse_quotes(cls, path: str) -> List[QuoteModel]:
        """Parse the csv file into a list of QuoteModel objects.

        Each line from the file should be a new quote, and the
        function will split out the author and body.
        """
        if not cls.can_ingest(path):
            raise Exception('incompatible file type')

        quotes = []
        doc = pandas.read_csv(path, sep=',')
        # print(doc)

        for index, row in doc.iterrows():
            quote = QuoteModel(author=row['author'], body=row['body'])
            quotes.append(quote)

        return quotes
