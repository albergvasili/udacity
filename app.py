"""Generate a random or a user defined meme on a flask app"""
import random
import os
import requests
from QuoteEngine import Ingestor
from flask import Flask, render_template, abort, request
import MemeGenerator
from meme import generate_meme

app = Flask(__name__)

meme = MemeGenerator.MemeGenerator('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']
    quotes = []
    for files in quote_files:
        quote = Ingestor.parse(files)
        quotes.append(quote)

    images_path = "./_data/photos/dog/"

    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote[0], quote[1])
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    img_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']
    response = requests.get(img_url, stream=True).content

    temp_img = './temp_img.jpg'

    with open(temp_img, 'wb') as f:
        f.write(response)

    os.remove(temp_img)
    path = meme.make_meme(temp_img, body, author)
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
