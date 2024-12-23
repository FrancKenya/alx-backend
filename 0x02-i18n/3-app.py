#!/usr/bin/env python3
"""Displays the use of gettext and _ to parametrize templates"""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _
#: _ is an alias for the gettext function that marks strings for translation


class Config:
    """Configuration class for the flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Determines the best match for the supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Function rendering the index page"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
