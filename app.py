"""Implement a flask app for the meme generator.

This will generate a random meme from the stock resources by default,
and also allow users to generate their own meme from a url and quote
of their choice.

to start the server:
export FLASK_APP=app.py
flask run --host 0.0.0.0 --port 3000 --reload
"""

import random
import os
import requests
from flask import Flask, render_template, abort, request
from MemeEngine import MemeEngine
from QuoteEngine import Ingestor
from QuoteEngine import QuoteModel


app = Flask(__name__)

meme = MemeEngine('./static/')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse_quotes(f))

    images_path = "./_data/photos/dog/"

    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author, dynamic_out=False)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.
    print(request.form['image_url'])
    url_img = requests.get(request.form['image_url'])
    save_path = 'static/url_image.jpg'

    with open(save_path, 'wb') as f:
        f.write(url_img.content)

    quote = QuoteModel(request.form['author'], request.form['body'])
    path = meme.make_meme(save_path, quote.body, quote.author)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
