#!/usr/bin/python3
"""
handler
"""
from api.v1.views import app_views
from flask import jsonify
from models import db_session
from models.user import User


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def statusOk():
    """ handler returning status """
    return jsonify({'status': 'OK'})

@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """ stats handler """
    count = len(db_session.query(User).all())
    return jsonify({'users': count})
