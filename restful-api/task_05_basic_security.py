#!/usr/bin/python3
"""
Module for API Security and Authentication Techniques.
This module demonstrates Basic Auth and JWT Authentication with RBAC.
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt
)

app = Flask(__name__)
auth = HTTPBasicAuth()

# Configuration for JWT
app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)

# In-memory user store as per specifications
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """Verifies the user credentials for Basic Authentication.

    Args:
        username (str): The username provided.
        password (str): The plain-text password provided.

    Returns:
        str: The username if verification is successful, None otherwise.
    """
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return username
    return None


@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """Endpoint protected by Basic Authentication.

    Returns:
        str: A success message if authenticated.
    """
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """Endpoint to authenticate user and return a JWT token.

    Expects:
        JSON payload with 'username' and 'password'.

    Returns:
        Response: JSON containing access_token or error message with 401.
    """
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = users.get(username)

    if user and check_password_hash(user['password'], password):
        # Embed roles within the JWT token payload
        access_token = create_access_token(
            identity=username,
            additional_claims={"role": user['role']}
        )
        return jsonify(access_token=access_token)

    return jsonify({"error": "Invalid credentials"}), 401


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """Endpoint protected by JWT Authentication.

    Returns:
        str: A success message if token is valid.
    """
    return "JWT Auth: Access Granted"


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """Endpoint accessible only by users with 'admin' role.

    Returns:
        Response: Success message if admin, or 403 Forbidden error.
    """
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


# --- Custom JWT Error Handlers as required by the Task ---

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handler for missing or invalid token."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handler for invalid token."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Handler for expired token."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """Handler for revoked token."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Handler for fresh token requirement."""
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
    app.run()
