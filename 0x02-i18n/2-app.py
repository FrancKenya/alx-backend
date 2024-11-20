#!/usr/bin/env python3
"""
Uses babel.localeselector decorator to create a function that
determines the best match
"""

from flask import Flask, render_template, request
from flask_babel import Babel, localeselector


class Config:
    """Configuration class for the flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@localeselector
def get_locale():
    """Determines the best match for the supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Function rendering the index page with the welcome message"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
