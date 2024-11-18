#!/usr/bin/env python3
"""
A basic flask app that uses a single route and renders template
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """Function rendering the index page with the welcome message"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
