"""Generic ingestor that handles any file type."""


from .IngestorInterface import IngestorInterface
from .TXTIngestor import TXTIngestor
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor
from .CSVIngestor import CSVIngestor
from .QuoteModel import QuoteModel
from typing import List


class Ingestor(IngestorInterface):
    """Generic ingestor that handles any file type.

    This leverages the separate txt, docx, pdf, and csv ingestors and
    uses the appropriate one based on the file extension
    """

    allowed_extensions = ['txt', 'docx', 'pdf', 'csv']

    @classmethod
    def parse_quotes(cls, path: str) -> List[QuoteModel]:
        """Extract quotations line by line from the document.

        Try each allowable extension type using the appropriate class.
        """
        if not cls.can_ingest(path):
            raise Exception('incompatible file type')

        ingestors = [TXTIngestor, DocxIngestor, PDFIngestor, CSVIngestor]
        for ingestor in ingestors:
            if not ingestor.can_ingest(path):
                continue
            else:
                return ingestor.parse_quotes(path)
