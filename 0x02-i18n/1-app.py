#!/usr/bin/env python3
"""
A flask app with babel
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Configuration class for the flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """Function rendering the index page with the welcome message"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
