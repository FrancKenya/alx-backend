#!/usr/bin/env python3
"""
Flask application to demonstrate user login emulation with Babel translations.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext
from typing import Optional, Dict

app = Flask(__name__)


class Config:
    """Flask app configuration class."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)

# Mocked user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(login_as: Optional[str]) -> Optional[Dict]:
    """
    Retrieve user from the mocked user table.
    Args:
        login_as (str): User ID passed as string in the `login_as` parameter.
    Returns:
        dict or None: User dictionary if found, otherwise None.
    """
    if not login_as or not login_as.isdigit():
        return None
    return users.get(int(login_as))


@app.before_request
def before_request():
    """
    Set the logged-in user in the global `flask.g` object.

    Fetches the user ID from the `login_as` URL parameter and sets
    the user in the `g` global object.
    """
    login_as = request.args.get('login_as')
    g.user = get_user(login_as)


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match for supported languages.

    It first checks the `locale` query parameter in the request. If the
    locale is supported, it is returned. Otherwise, it defaults to the
    best match based on the request headers.
    """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Render the home page with dynamic welcome message."""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
