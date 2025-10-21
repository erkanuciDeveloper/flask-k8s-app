from flask import Flask, jsonify, request
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB bağlantısı
mongo_host = os.environ.get('MONGO_HOST', 'localhost')
mongo_port = int(os.environ.get('MONGO_PORT', 27017))
client = MongoClient(f'mongodb://{mongo_host}:{mongo_port}/')
db = client["flaskdb"]
collection = db["users"]

@app.route('/')
def home():
    return jsonify(message="Flask + MongoDB + Kubernetes!"), 200

@app.route('/users', methods=['GET'])
def get_users():
    users = list(collection.find({}, {"_id": 0}))
    return jsonify(users), 200

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    collection.insert_one(data)
    return jsonify(message="User added successfully!"), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
