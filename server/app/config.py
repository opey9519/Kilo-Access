import os
from dotenv import load_dotenv
from urllib.parse import quote

load_dotenv()


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # JWT Secret key for authentication - set this in .env
    JWT_SECRET_KEY = os.getenv(
        "JWT_SECRET_KEY", "dev-secret")  # fallback for local


class DevelopmentConfig(Config):
    DB_USER = os.getenv("DEV_DB_USER")
    DB_PASSWORD = quote(os.getenv("DEV_DB_PASSWORD", ""))
    DB_HOST = os.getenv("DEV_DB_HOST")
    DB_PORT = os.getenv("DEV_DB_PORT")
    DB_NAME = os.getenv("DEV_DB_NAME")
    DB_URL = os.getenv("DEV_DB_URL")
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"  # Testing
    SECRET_KEY = "test"


class ProductionConfig(Config):
    # Database credentials from environment variables
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = quote(os.getenv("DB_PASSWORD", ""))
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")
    DB_URL = os.getenv("DB_URL")
    # Connection string SQLAlchemy uses to connect to PostgreSQL
    SQLALCHEMY_DATABASE_URI = DB_URL
