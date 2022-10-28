import random
import os
import requests
from MemeEngine import MemeEngine
from QuoteEngine import Ingestor, QuoteModel
from flask import Flask, render_template, abort, request
import QuoteEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for file in quote_files:
        quotes.extend(Ingestor.parse(file))

    images_path = "./_data/photos/dog/"
    imgs = []
    for file in os.listdir(images_path):
        imgs.append(os.path.join(images_path, file))

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    img = random.choice(imgs)
    quote = random.choice(quotes)
    print(meme.make_meme(img, quote.body, quote.author))
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    url = request.form['image_url']
    try:
        image = requests.get(url)
        form_body, form_author = request.form['body'], request.form['author']
        quote = QuoteModel(form_body, form_author)
        tmp_path = f'./tmp/{random.randint(900000,10000000)}.png'
        with open(tmp_path, 'wb') as file:
            file.write(image.content)
        path = meme.make_meme(tmp_path, form_body, form_author)
        return render_template('meme.html', path=path)
    except Exception:
        return render_template('error.html')


if __name__ == "__main__":
    app.run()
