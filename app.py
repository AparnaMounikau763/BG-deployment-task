from flask import Flask, jsonify
import os
import socket
from datetime import datetime

app = Flask(__name__)

# Deployment Environment (Blue or Green)
VERSION = os.getenv("VERSION", "blue")

HOSTNAME = socket.gethostname()


@app.route("/")
def home():
    return jsonify({
        "application": "Blue-Green Deployment Demo",
        "environment": VERSION.upper(),
        "hostname": HOSTNAME,
        "status": "Application is running",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "UP",
        "environment": VERSION.upper()
    }), 200


@app.route("/version")
def version():
    return jsonify({
        "environment": VERSION.upper()
    })


@app.route("/info")
def info():
    return jsonify({
        "Application": "Flask Blue-Green Deployment",
        "Environment": VERSION.upper(),
        "Hostname": HOSTNAME,
        "Python": "Flask",
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)