#!/usr/bin/python3
from flask import Flask
from flask import jsonify
from flask import request
from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash


from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = "clave-super-secreta-2.0"
jwt = JWTManager(app)
auth = HTTPBasicAuth()

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin": {"username": "admin1", "password": generate_password_hash("admin_password"),"role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users[username].get('password'), password):
        return users.get(username)
    return None
    
@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

@app.route("/login", methods=["POST"])
def login():
    user = request.get_json()
    username = request.json.get("username")
    password = request.json.get("password")

    if users and check_password_hash(user[username].get('password'), password):
        access_token = create_access_token(
            identity={"username": username, "role": users["role"].get(username)})
        return jsonify(access_token=access_token)
    return jsonify({'error': "data invalid"}), 401

@app.route("/jwt-protected")
@jwt_required()
def protected():
    return "JWT Auth: Access Granted"

@app.route("/admin-only")
@jwt_required()
def admin():
    current_user = get_jwt_identity()
    if current_user["role"] == "admin":
        return "Admin Access: Granted"
    return jsonify({"error": "Admin access required"}), 403

if __name__ == '__main__':
    app.run(debug=True)