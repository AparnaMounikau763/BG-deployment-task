import os

class Config:
    APP_NAME = "Flask Blue Green"
    VERSION = os.getenv("APP_VERSION", "v1")
    ENVIRONMENT = os.getenv("FLASK_ENV", "production")

config = Config()
