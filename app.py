from flask import Flask, jsonify
import os

app = Flask(__name__)

VERSION = os.getenv("VERSION", "BLUE")

@app.route("/")
def home():
    return f"<h1>{VERSION} Environment</h1>"

@app.route("/health")
def health():
    return jsonify({
        "status": "UP",
        "version": VERSION
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)