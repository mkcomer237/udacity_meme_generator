"""Callable IngestorInterface subclass that parses pdf files."""


from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List
import subprocess


class PDFIngestor(IngestorInterface):
    """Import and parse pdf files into QuoteModel objects."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse_quotes(cls, path: str) -> List[QuoteModel]:
        """Parse the pdf file into a list of QuoteModel objects.

        Each line from the file should be a new quote, and the
        function will split out the author and body.  Uses subprocess
        and the pdftotext service to convert pdf, and then parses
        the result of the sdtout.  
        """
        if not cls.can_ingest(path):
            raise Exception('incompatible file type')

        quotes = []
        p = subprocess.run(['pdftotext', path, '-'], stdout=subprocess.PIPE)
        doc = p.stdout.decode("utf-8")

        for row in doc.split(' "'):
            body, author = row.split('-')
            body = body.replace('"', '')
            quote = QuoteModel(author=author.strip(), body=body.strip())
            quotes.append(quote)

        return quotes
