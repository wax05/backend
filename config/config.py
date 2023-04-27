import os
from datetime import timedelta

class BaseConfig:
    DEBUG = False
    TESTING = False
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=1)
class ProductConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
    SESSION_COOKIE_HTTPONLY = True
    SECRET_KEY = os.getenv("SECRET_KEY")

class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    SECRET_KEY = "HI"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:1234@localhost:3306/test_db"#TestConfig