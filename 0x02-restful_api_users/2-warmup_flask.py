#!/usr/bin/python3
"""
warmup flask application
"""
from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def hbntn():
    """ / method """
    app.url_map.strict_slashes = False
    return "Holberton School"


@app.route('/c')
def cisfun():
    """ /c method """
    app.url_map.strict_slashes = False
    return "C is fun!"


if __name__ == "__main__":
    h = os.getenv('HBNB_API_HOST')
    p = int(os.getenv('HBNB_API_PORT'))
    app.run(host=h, port=p)
