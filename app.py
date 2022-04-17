"""Use requests package to fetch an image from a submitted URL."""

import random
import os
import requests
from QuoteEngine import Ingestor
from flask import Flask, render_template, abort, request
import MemeGenerator
from meme import generate_meme

# @TODO Import your Ingestor and MemeEngine classes

app = Flask(__name__)

meme = MemeGenerator.MemeGenerator('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']
    quotes = []
    # TODO: Use the Ingestor class to parse all files in the
    # quote_files variable
    for files in quote_files:
        quote = Ingestor.parse(files)
        quotes.append(quote)

    images_path = "./_data/photos/dog/"

    # TODO: Use the pythons standard library os class to find all
    # images within the images images_path directory
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    # @TODO:
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
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
    img_url = request.form['image_url']
    body = request.form['body']
    author = request.form['body']
    response = requests.get(img_url, tream=True).content

    temp_img = './temp_img.jpg'

    with open(temp_img, 'wb') as f:
        f.write(response)

    os.remove(temp_img)
    path = generate.meme(temp_img, body, author)
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
