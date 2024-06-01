#!/usr/bin/python3

from flask import Flask, jsonify, request
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
user = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"},"jorge": {"name": "Jorge", "age": 21, "city": "Los Angeles"}}
@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def get_data():
    return jsonify(list(user.keys()))

@app.route('/status')
def get_stutas():
    return "OK"

if __name__ == "__main__":
    app.run(debug=True)