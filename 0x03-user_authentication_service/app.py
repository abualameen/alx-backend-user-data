#!/usr/bin/env python3
"""
Register user end-point
"""
from flask import Flask, jsonify, request
from auth import Auth

app = Flask(__name__)
AUTH = Auth()

@app.route('/users', methods=['POST'])
def register_user():
    """Register user end-point"""
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
