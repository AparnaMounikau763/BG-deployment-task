import os

class Config:
    APP_NAME = "Flask Blue Green - V2"
    VERSION = os.getenv("APP_VERSION", "v2")
    ENVIRONMENT = os.getenv("FLASK_ENV", "production")

config = Config()
