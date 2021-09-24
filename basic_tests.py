"""Script to run and test out classes as they are built out."""


from QuoteEngine import DocxIngestor
from QuoteEngine import IngestorInterface
from QuoteEngine import QuoteModel
import docx

test_quote = QuoteModel(author='Max', body='I love python')
print(test_quote)

# print(IngestorInterface.parse_quotes('._data/dogquotes/DogQuotesDOCX.docx'))

doc = docx.Document('_data/DogQuotes/DogQuotesDOCX.docx')

try:
    print(DocxIngestor.parse_quotes('._data/DogQuotes/DogQuotesCSV.csv'))
except(Exception):
    print('Throws an error as expected')

print(DocxIngestor.parse_quotes('_data/DogQuotes/DogQuotesDOCX.docx'))
