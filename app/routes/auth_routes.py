from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.user import User
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST', 'OPTIONS'])
def login():
    if request.method == 'OPTIONS':
        return jsonify({}), 200
    
    data = request.get_json()
    
    user = User.query.filter_by(email=data.get("email")).first()
    
    if not user or not user.check_password(data.get("password")):
        return jsonify({"error": "Invalid credentials"}), 401
    
    token = create_access_token(identity={"id": user.id, "role": user.role})
    
    return jsonify({"access_token": token}), 200