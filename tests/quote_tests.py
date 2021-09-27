"""Script to run and test out classes as they are built out."""
import sys
sys.path.append('/Users/maxcomer/Dropbox/coding_and_cs/intermediate_python/meme_generator')  # noqa
from QuoteEngine import DocxIngestor
from QuoteEngine import IngestorInterface
from QuoteEngine import QuoteModel
from QuoteEngine import CSVIngestor
from QuoteEngine import PDFIngestor
from QuoteEngine import TXTIngestor
from QuoteEngine import Ingestor
import docx

test_quote = QuoteModel(author='Max', body='I love python')
print(test_quote)

print(IngestorInterface.parse_quotes('_data/dogquotes/DogQuotesDOCX.docx'))

doc = docx.Document('_data/DogQuotes/DogQuotesDOCX.docx')

try:
    print(DocxIngestor.parse_quotes('_data/DogQuotes/DogQuotesCSV.csv'))
    raise Exception('did not throw an error')
except(Exception):
    print('Throws an error as expected')

print(DocxIngestor.parse_quotes('_data/DogQuotes/DogQuotesDOCX.docx'))


try:
    print(CSVIngestor.parse_quotes('_data/DogQuotes/DogQuotesDOCX.docx'))
    raise Exception('did not throw an error')
except(Exception):
    print('Throws an error as expected')

print(CSVIngestor.parse_quotes('_data/DogQuotes/DogQuotesCSV.csv'))


try:
    print(PDFIngestor.parse_quotes('_data/DogQuotes/DogQuotesDOCX.docx'))
    raise Exception('did not throw an error')
except(Exception):
    print('Throws an error as expected')

print(PDFIngestor.parse_quotes('_data/DogQuotes/DogQuotesPDF.pdf'))


try:
    print(TXTIngestor.parse_quotes('_data/DogQuotes/DogQuotesDOCX.docx'))
    raise Exception('did not throw an error')
except(Exception):
    print('Throws an error as expected')

print(TXTIngestor.parse_quotes('_data/DogQuotes/DogQuotesTXT.txt'))


print('\nNow testing the universal ingestor:')
print(Ingestor.parse_quotes('_data/DogQuotes/DogQuotesTXT.txt'))
print(Ingestor.parse_quotes('_data/DogQuotes/DogQuotesDOCX.docx'))
print(Ingestor.parse_quotes('_data/DogQuotes/DogQuotesPDF.pdf'))
print(Ingestor.parse_quotes('_data/DogQuotes/DogQuotesCSV.csv'))
