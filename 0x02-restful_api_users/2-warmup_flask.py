#!/usr/bin/python3
"""
warmup flask application
"""
from flask import Flask
import os
app = Flask(__name__)
app.url_map.strict_slashes = False
h = os.getenv('HBNB_API_HOST')
p = int(os.getenv('HBNB_API_PORT'))


@app.route('/', methods=['GET'])
def hbntn():
    """ / method """
    return 'Holberton School'

@app.route('/c', methods=['GET'])
def cisfun():
    """ /c method """
    return 'C is fun!'

if __name__ == '__main__':
    app.run(host=h, port=p)
