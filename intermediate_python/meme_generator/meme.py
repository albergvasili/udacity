"""Generate a meme from the command line."""
import os
import random
import argparse
from QuoteEngine import QuoteModel, Ingestor
import MemeGenerator


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given a path and a quote."""
    img = None
    quote = None

    if not os.path.isdir('tmp'):
        os.makedirs('tmp')

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
            quote = (Ingestor.parse(f))
            quotes.extend(quote)

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel.QuoteModel(body, author)

    meme = MemeGenerator.MemeGenerator('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('--body', type=str, help="string quote body")
    parser.add_argument('--author', type=str, help="string quote author")
    parser.add_argument('--path', type=str, help="path to image file")
    args = parser.parse_args()
    body = args.body
    author = args.author
    path = args.path
    print(generate_meme(args.path, args.body, args.author))
