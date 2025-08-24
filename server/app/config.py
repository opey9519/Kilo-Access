import os
from dotenv import load_dotenv
from urllib.parse import quote

load_dotenv()

# Database credentials from environment variables
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = quote(os.getenv("DB_PASSWORD"))
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Connection string SQLAlchemy uses to connect to PostgreSQL
SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# Disables Flask-SQLAlchemy event tracking for performance
SQLALCHEMY_TRACK_MODIFICATIONS = False

# JWT Secret key for authentication - set this in .env
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
