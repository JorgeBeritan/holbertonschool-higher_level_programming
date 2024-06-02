#!/usr/bin/python3

from flask import Flask, jsonify, request
import json
app = Flask(__name__)
app.json.sort_keys = False

users = {}

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Flask API!"

@app.route('/data', methods=['GET'])
def get_data():
    response = jsonify(list(users.keys()))
    return response

@app.route('/user/<username>', methods=['GET'])
def get_user(username):
    if username in users:
        response = jsonify(users[username])
        return response
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST', 'GET'])
def add_user():
    data = request.get_json()
    username = data.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201

@app.route('/status')
def get_stutas():
    return "OK"

if __name__ == "__main__":
    app.run(debug=True)