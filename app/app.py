
from flask import Flask, render_template, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB bağlantısı
MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo-service:27017/")
client = MongoClient(MONGO_URI)
db = client.get_database("flaskdb")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check_mongo")
def check_mongo():
    try:
        db.command("ping")
        return jsonify({"status": "connected"})
    except Exception:
        return jsonify({"status": "disconnected"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

