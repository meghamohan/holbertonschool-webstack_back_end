#!/usr/bin/python3
"""
handler
"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def statusOk():
    """ handler returning status """
    return jsonify({'status': 'OK'})
