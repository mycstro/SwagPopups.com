# __init__.py

import os
import logging

from flask import Flask, session
from flask_session import Session
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_migrate import Migrate

# Import your config classes
from .config import DevelopmentConfig  # or ProductionConfig, etc.

# Initialize extensions
db = SQLAlchemy()
bootstrap = Bootstrap()
bcrypt = Bcrypt()
csrf = CSRFProtect()
migrate = Migrate()  # <-- Migrate extension
api = Api()

def create_app(config_class=DevelopmentConfig):
    """
    Factory function to create and configure the Flask application.
    """
    app = Flask(__name__)
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)

    # ------------------- Logging Configuration -------------------
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler()]
    )
    logger = logging.getLogger(__name__)
    # ------------------------------------------------------------

    # ------------------- Basic Config ---------------------------
    # Cross-Origin Resource Sharing
    CORS(app)
    app.config.from_object(config_class)

    # Secret key for sessions and CSRF protection
    #app.config['SECRET_KEY'] = 'your_secret_key_here'
    
    # Database config (SQLite as an example)
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///membership.db'
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # ------------------------------------------------------------

    # ------------------ Initialize Extensions -------------------
    db.init_app(app)
    bootstrap.init_app(app)
    bcrypt.init_app(app)
    csrf.init_app(app)
    api.init_app(app)
    
    # Initialize Flask-Migrate with our app and database
    migrate.init_app(app, db)
    # ------------------------------------------------------------

    # ------------------- Blueprint Registration -----------------
    from .routes import main  # Your blueprint from routes.py
    app.register_blueprint(main)
    # If you have other blueprints, register them here as well:
    # from .another_module import another_blueprint
    # app.register_blueprint(another_blueprint)
    # ------------------------------------------------------------

    return app
