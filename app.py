from flask import Flask
from flask import render_template, url_for

#
import os
import random

#
import sys
from importlib import import_module

app = Flask(__name__)

@app.route('/')
def index():
    # Pick a book
    temp_book = random.choice(os.listdir('static/quotes/'))
    temp_bookname = os.path.splitext(temp_book)[0]
    while temp_bookname.split('_')[0] != 'book':
        temp_book = random.choice(os.listdir('static/quotes/'))
        temp_bookname = os.path.splitext(temp_book)[0]
    # book_to_import = import_module('static.quotes.' + temp_bookname)

    # For testing, fix book number
    book_to_import = import_module('static.quotes.book_' + '02')


    # Pick a quote
    temp_quote_list = book_to_import.quotes_list
    temp_quote = random.choice(temp_quote_list)

    # For testing, fix quote index
    temp_quote = temp_quote_list[22]


    #  Pick an image
    temp_image = random.choice(os.listdir('static/images/'))
    while temp_image.endswith('.DS_Store'):
        temp_image = random.choice(os.listdir('static/images/'))
    temp_image = 'images/' + temp_image

    # For testing
    # temp_image = 'images/marcus_aurelius_noir.jpeg'

    return render_template("index.html", quote=temp_quote, image=temp_image)

@app.route('/About/')
def about():
    return render_template("about.html")

@app.route('/Contact/')
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run()
