from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from datetime import timedelta
from config import DevelopmentConfig, ProductionConfig, TestingConfig
import os

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()


def create_app():
    app = Flask(__name__)
    env = os.getenv("FLASK_ENV", "development")

    # Database Configurations
    if env == "production":
        app.config.from_object(ProductionConfig)
    elif env == "testing":
        app.config.from_object(TestingConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    # JWT Expirations
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=20)
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # CORS setup
    CORS(app, origins=[
        "http://localhost:5173",  # local Vite dev
        "https://kilo-access-git-dbprod-gavins-projects-bf44ff82.vercel.app",  # Vercel preview
        "https://kilo-access.vercel.app"  # production domain
    ])

    from .api.auth import auth_bp
    from .api.admin import admin_bp
    from .api.user import user_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(user_bp)

    # Only create tables in dev/testing
    if env in ["development", "testing"]:
        with app.app_context():
            db.create_all()

    return app
