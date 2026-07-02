from flask import Flask, jsonify
import os
import socket
from datetime import datetime

app = Flask(__name__)

# Read deployment version from environment variable
VERSION = os.getenv("VERSION", "blue")

HOSTNAME = socket.gethostname()


@app.route("/")
def home():

    return jsonify({
        "message": f"Welcome to {VERSION.upper()} Environment",
        "environment": VERSION,
        "hostname": HOSTNAME,
        "status": "Running",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })


@app.route("/health")
def health():

    return jsonify({
        "status": "UP",
        "environment": VERSION
    }), 200


@app.route("/version")
def version():

    return jsonify({
        "environment": VERSION
    })


@app.route("/info")
def info():

    return jsonify({
        "Application": "Blue Green Deployment Demo",
        "Environment": VERSION,
        "Hostname": HOSTNAME,
        "Python": "Flask",
        "Deployment": VERSION.upper(),
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)