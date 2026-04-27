from flask import Flask
from flask_cors import CORS
from .config import Config
from .extensions import db, migrate, jwt
from app.routes.animal_routes import animal_bp
from app.routes.vaccination_routes import vaccination_bp
from app.routes.auth_routes import auth_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # ✅ CORS fix
    CORS(app, 
         origins=["http://localhost:5173", "http://127.0.0.1:5173"],
         supports_credentials=True,
         allow_headers=["Content-Type", "Authorization"],
         methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])
    
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    app.register_blueprint(animal_bp, url_prefix="/api/animals")
    app.register_blueprint(vaccination_bp, url_prefix="/api/vaccinations")
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    
    return app