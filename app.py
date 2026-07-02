from flask import Flask, jsonify
import os
import socket
import threading
import time
from datetime import datetime

app = Flask(__name__)

VERSION = os.getenv("VERSION", "BLUE")
HOSTNAME = socket.gethostname()

healthy = True


def simulate_failure():
    global healthy

    # Wait 30 seconds after startup
    time.sleep(30)

    # Simulate application failure
    healthy = False

    print("Application became unhealthy.")


# Start background thread
threading.Thread(target=simulate_failure, daemon=True).start()


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

    if healthy:
        return jsonify({
            "status": "UP",
            "environment": VERSION.upper()
        }), 200

    return jsonify({
        "status": "DOWN",
        "environment": VERSION.upper()
    }), 500


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