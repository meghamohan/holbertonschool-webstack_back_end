#!/usr/bin/python3
"""
api app
"""
from api.v1.views import app_views
from flask import Flask, jsonify
import os

app = Flask(__name__)
app.register_blueprint(app_views)

@app.errorhandler(404)
def page_not_found(e):
    """ 404 handler """
    return jsonify({'error': 'Not found'}), 404

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    h = os.getenv('HBNB_API_HOST')
    p = int(os.getenv('HBNB_API_PORT'))
    app.run(host=h, port=p)
