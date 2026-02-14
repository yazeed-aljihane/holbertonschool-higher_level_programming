#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

storge = {'khalid': {"username": "Jane", "age": 28, "city": "Los Angeles"},
            'yazeed': {"username": "yazeed", "age": 25, "city": "Los"}
            }
@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/data')
def data():
    return jsonify(list(storge.keys()))


@app.route('/status')
def status():
    return "ok"

@app.route("/users/<username>")
def users(username):
    if storge.get(username) == None:
        return jsonify({"error": "User not found"}), 404
    else:
        return jsonify(storge[username]), 200

@app.route("/add_user", methods = ['POST'])
def add_user():
    if request.get_json(silent = True) != None:
        data = request.get_json()
        if data.get('username') != None:
            username = data.get('username')
            if username in storge:
                return jsonify({"error":"Username already exists"}), 409
            else:
                storge[username] = data
                return jsonify({"message": "User added", "user": data}), 201
        else:
            return jsonify({"error":"Username is required"}), 400
    else:
        return jsonify({"error":"Invalid JSON"}), 400









if __name__ == '__main__':
    app.run(debug = True)
