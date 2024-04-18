#!/usr/bin/env python3
""" Module for """
from flask import request, jsonify
# from api.v1.app import app # auth  # Import app from Flask instance
from models.user import User
from api.v1.views import app_views


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
@app_views.route('/auth_session/login/',
                 methods=['POST'], strict_slashes=False)
def session_login():
    email = request.form.get('email')
    password = request.form.get('password')
    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400
    user = User.search({"email": email})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    user_data = user.to_json()
    user_data["session_id"] = session_id
    response = jsonify(user_data)
    response.set_cookie(auth.SESSION_NAME, session_id)
    return response, 200
