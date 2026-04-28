from flask import Flask
from flask_cors import CORS
from .config import Config
from .extensions import db, migrate, jwt
from app.routes.animal_routes import animal_bp
from app.routes.auth_routes import auth_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # ✅ Simple but complete CORS
    CORS(app, 
         origins="http://localhost:5173",
         methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
         allow_headers=["Content-Type", "Authorization"],
         supports_credentials=True)
    
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    # ✅ Register blueprints WITHOUT trailing slashes in URL
    app.register_blueprint(animal_bp, url_prefix='/api/animals')
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    
    return app