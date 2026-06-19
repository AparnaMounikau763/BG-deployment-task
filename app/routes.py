from flask import Blueprint, jsonify
from .config import config

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def home():
    return jsonify({
        "message": "Flask Blue-Green Deployment - v2",
        "version": config.VERSION,
        "environment": config.ENVIRONMENT
    })

@main_bp.route("/health")
def health():
    return jsonify({"status": "UP"}), 200

@main_bp.route("/version")
def version():
    return jsonify({"version": config.VERSION})
