"""Callable IngestorInterface subclass that parses docx files."""


from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List
import docx


class DocxIngestor(IngestorInterface):
    """Import and parse docx files into QuoteModel objects."""

    allowed_extensions = ['docx']

    @classmethod
    def parse_quotes(cls, path: str) -> List[QuoteModel]:
        """Parse the docx file into a list of QuoteModel objects.

        Each line from the file should be a new quote, and the
        function will split out the author and body.
        """
        if not cls.can_ingest(path):
            raise Exception('incompatible file type')

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text == '':
                continue
            body, author = tuple(para.text.split('-'))
            quote = QuoteModel(author.strip(), body.replace('"', '').strip())
            quotes.append(quote)

        return quotes
