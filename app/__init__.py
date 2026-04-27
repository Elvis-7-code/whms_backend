from flask import Flask
from flask_cors import CORS
from .config import Config
from .extensions import db, migrate, jwt
from app.routes.animal_routes import animal_bp
from app.routes.breeding_routes import breeding_bp
from app.routes.vaccination_routes import vaccination_bp
from app.routes.auth_routes import auth_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # ✅ MOST PERMISSIVE CORS — for development only
    CORS(app, 
         origins="*",
         supports_credentials=True,
         allow_headers=["*"],
         methods=["*"])
    
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    app.register_blueprint(animal_bp, url_prefix="/api/animals")
    app.register_blueprint(breeding_bp, url_prefix="/api/breedings")
    app.register_blueprint(vaccination_bp, url_prefix="/api/vaccinations")
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    
    return app