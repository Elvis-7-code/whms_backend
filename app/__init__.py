from flask import Flask
from .config import Config
from .extensions import db, migrate, jwt
from app.routes.animal_routes import animal_bp
from app.routes.breeding_routes import breeding_bp
from app.routes.vaccination_routes import vaccination_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///whms.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'super-secret-key'
    app.config.from_object("app.config.Config")

    app.register_blueprint(animal_bp, url_prefix="/api/animals")
    app.register_blueprint(breeding_bp, url_prefix="/api/breedings")
    app.register_blueprint(vaccination_bp, url_prefix="/api/vaccinations")

    from . import models
    
    return app

