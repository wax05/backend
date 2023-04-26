import os

class BaseConfig:
    DEBUG = False
    TESTING = False

class ProductConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
    SESSION_COOKIE_HTTPONLY = True
    SECRET_KEY = os.getenv("SECRET_KEY")

class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite3"#TestConfig