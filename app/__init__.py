from flask import Flask
from .config import Config
from .extensions import db, migrate, jwt
from app.routes.animal_routes import animal_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    app.register_blueprint(animal_bp, url_prefix="/api/animals")

    return app