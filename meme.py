"""Generate memes."""

import os
import random
from argparse import ArgumentParser
from QuoteEngine import Ingestor
from MemeEngine import MemeEngine
from QuoteEngine import QuoteModel


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote."""
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse_quotes(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(author, body)

    meme = MemeEngine('./memes/')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    """Script to run the meme generator via the command line.

    Takes a photo to memify, and optional arguments for quote body and
    author.
    """

    parser = ArgumentParser(description='Parse meme generation parameters')

    parser.add_argument('path',
                        type=str,
                        help='required filepath for input image')
    parser.add_argument('--body',
                        type=str,
                        help='optional quote body')
    parser.add_argument('--author',
                        type=str,
                        help='quote author (required if body is specified)')
    args = parser.parse_args()

    # print(generate_meme('_data/photos/dog/xander_1.jpg', None, None))
    print(generate_meme(args.path, args.body, args.author))
