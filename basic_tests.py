"""Script to run and test out classes as they are built out."""


from QuoteEngine import IngestorInterface
from QuoteEngine import QuoteModel

test_quote = QuoteModel(author='Max', body='I love python')
print(test_quote)

print(IngestorInterface.parse_quotes('/data/dogquotes/DogQuotes.docx'))
