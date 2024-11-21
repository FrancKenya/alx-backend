#!/usr/bin/env python3
"""Displays the use of gettext and _ to parametrize templates"""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _

_: """
Alias for the gettext function provided by Flask-Babel.

Use this function to mark strings for translation in
the templates or Python code.
"""


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
    """
    Determines the best match for the supported languages.

    It first checks for the `locale` query parameter in the request. If
    the locale is supported, it is returned. Otherwise, it defaults
    to the best match based on the request headers.
    """
    # starts with checking for the locale query parameters
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    # Handke when locale not matched by reverting to default language
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Function rendering the index page with the welcome message"""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
