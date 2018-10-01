#!/usr/bin/python3
"""
warmup flask application
"""
from flask import Flask
app = Flask(__name__)


@app.route('/c', methods=['GET'])
def index():
    """ root definition """
    app.url_map.strict_slashes = False
    return 'C is fun!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
