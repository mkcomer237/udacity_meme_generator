"""Script to run and test out classes as they are built out."""


from QuoteEngine import DocxIngestor
from QuoteEngine import IngestorInterface
from QuoteEngine import QuoteModel
from QuoteEngine import CSVIngestor
from QuoteEngine import PDFIngestor
import docx

test_quote = QuoteModel(author='Max', body='I love python')
print(test_quote)

print(IngestorInterface.parse_quotes('_data/dogquotes/DogQuotesDOCX.docx'))

doc = docx.Document('_data/DogQuotes/DogQuotesDOCX.docx')

try:
    print(DocxIngestor.parse_quotes('_data/DogQuotes/DogQuotesCSV.csv'))
except(Exception):
    print('Throws an error as expected')

print(DocxIngestor.parse_quotes('_data/DogQuotes/DogQuotesDOCX.docx'))

print(CSVIngestor.parse_quotes('_data/DogQuotes/DogQuotesCSV.csv'))

print(PDFIngestor.parse_quotes('_data/DogQuotes/DogQuotesPDF.pdf'))
