import os
import logging
from flask import Flask, jsonify

app = Flask(__name__)

# Configuration
APP_NAME = "Flask Blue Green - V2"
VERSION = os.getenv("APP_VERSION", "v2")
ENVIRONMENT = os.getenv("FLASK_ENV", "production")

# Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)


@app.route("/")
def home()
    return jsonify({
        "message": "Flask Blue-Green Deployment - v2",
        "version": VERSION,
        "environment": ENVIRONMENT
    })


@app.route("/health")
def health():
    return jsonify({"status": "UP"}), 200


@app.route("/version")
def version():
    return jsonify({
        "version": VERSION
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)