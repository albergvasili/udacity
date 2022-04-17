# Meme Generator

This is a Udacity project from the course 'Intermediate Python'

## Project Overview:
Build a meme generator - a multimedia application to dynamically generate memes, including an image with an overlaid quote.

## Instructions:
The module QuoteEngine checks pdf, csv, txt, and docx files to extract the author and the text from a quote. Each file type is parsed using a specific ingestor. A main ingestor class (Ingestor.py) automatically chooses the module to be used, based on the file extension.

The MemeGenerator.py script modifies an image file to add the text parsed by the QuoteEngine module.

Meme.py is used to create a meme from the command line using the argparse library. The optinal arguments provided define the _body_ of the quote, its _author_ and the _path_ of the image file.

The code includes a flask app (app.py) that generates a random meme, or a user defined meme.


