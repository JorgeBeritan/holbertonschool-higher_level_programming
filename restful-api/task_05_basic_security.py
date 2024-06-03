#!/usr/bin/python3

from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

app = Flask(__name__)

# Configuración de la clave secreta para JWT
app.config['JWT_SECRET_KEY'] = 'your_secret_key'  # Cambia esto a una clave secreta más segura

jwt = JWTManager(app)
auth = HTTPBasicAuth()

users = [
    {"username": "admin", "password": generate_password_hash('admin_password'), "rol": "admin"},
    {"username": "user", "password": generate_password_hash('user_password'), "rol": "user"}
]

@auth.verify_password
def verify_password(username, password):
    user = next((user for user in users if user["username"] == username), None)
    if user and check_password_hash(user["password"], password):
        return username

@app.route('/login', methods=["POST", "GET"])
def login():
    data = request.get_json()
    if not data or not data.get("username") or not data.get("password"):
        return jsonify({"message": "Missing username or password"}), 400
    
    username = data.get("username")
    password = data.get("password")
    user = next((user for user in users if user["username"] == username), None)
    if user and check_password_hash(user["password"], password):
        access_token = create_access_token(identity=username)
        return jsonify({"access_token": access_token}), 200
    
    return jsonify({"message": "Invalid credentials"}), 401

@app.route("/protected")
@jwt_required()
def protected_route():
    return jsonify({"message": "This is a protected route"}), 200

@app.route("/admin-only")
@jwt_required()
def admin_only_route():
    current_user = get_jwt_identity()
    user = next((user for user in users if user["username"] == current_user), None)
    if user and user["rol"] == "admin":
        return jsonify({"message": "This is an admin-only route"}), 200
    
    return jsonify({"message": "Unauthorized access"}), 403

if __name__ == "__main__":
    app.run(debug=True)
