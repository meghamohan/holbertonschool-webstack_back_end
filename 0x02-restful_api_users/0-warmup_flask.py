#!/usr/bin/python3
"""
warmup flask application
"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/', methods=['GET'])
def index():
    """ root definition """
    return 'Holberton School'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
