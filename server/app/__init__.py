# server/app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from datetime import timedelta
from .config import DevelopmentConfig, ProductionConfig, TestingConfig
import os

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()

# Create Flask App based on configuration environment


def create_app(flask_config="development"):
    app = Flask(__name__)

    # Database Configurations
    if flask_config == "production":
        app.config.from_object(ProductionConfig)
    elif flask_config == "testing":
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

    # Import and register blueprints
    from .api.auth import auth_bp
    from .api.admin import admin_bp
    from .api.user import user_bp
    from .api.health import health_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(health_bp)

    # Only create tables in dev/testing
    if flask_config in ["development", "testing"]:
        with app.app_context():
            db.create_all()

    return app
