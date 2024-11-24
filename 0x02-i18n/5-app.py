#!/usr/bin/env python3
"""
Flask application demonstrating Babel for translations and
a simple user login emulation using URL parameters.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext
from typing import Dict, Optional


def _(text: str) -> str:
    """
    Marks the given string for translation using gettext.
    Args:
        text (str): The text to be translated.
    Returns:
        str: The translated text.
    """
    return gettext(text)


class Config:
    """Configuration class for the flask app."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

# Mocked users table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(login_as: Optional[str]) -> Optional[Dict]:
    """
    Fetches the user from the mocked users table.
    Args:
        login_as (str): User ID passed as a string in the `login_as` parameter.
    Returns:
        dict or None: User dictionary if found, otherwise None.
    """
    if not login_as or not login_as.isdigit():
        return None
    return users.get(int(login_as))


@app.before_request
def before_request():
    """
    Set the logged-in user in the global flask.g object.

    The user is fetched from the mocked users table based on the
    `login_as` parameter in the request.
    """
    login_as = request.args.get('login_as')
    g.user = get_user(login_as)


@babel.localeselector
def get_locale() -> str:
    """
    Determines the best match for the supported languages.

    It first checks for the `locale` query parameter in the request. If
    the locale is supported, it is returned. Otherwise, it defaults
    to the best match based on the request headers.
    """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Render the index page with a dynamic welcome message."""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
