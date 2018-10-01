#!/usr/bin/python3
"""
warmup flask application
"""
from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/hbtn')
def index():
    """ /hbtn method """
    app.url_map.strict_slashes = False
    data = { "C": "is fun", 
            "Python": "is cool", 
            "Sysadmin": "is hiring"
    }
    return jsonify(data)


if __name__ == "__main__":
    h = os.getenv('HBNB_API_HOST')
    p = int(os.getenv('HBNB_API_PORT'))
    app.run(host=h, port=p)
