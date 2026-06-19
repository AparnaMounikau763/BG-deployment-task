from flask import Flask
from .config import config
from .routes import main_bp
import logging

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s"
    )

    app.register_blueprint(main_bp)

    return app
