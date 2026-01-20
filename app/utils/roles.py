from functools import wraps
from flask_jwt_extended import get_jwt_identity
from app.models.user import User
from flask import jsonify

def role_required(*allowed_roles):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            user_id = get_jwt_identity()
            user = User.query.get(user_id)

            if not user or user.role not in allowed_roles:
                return jsonify({"error": "Access denied"}), 403

            return fn(*args, **kwargs)
        return wrapper
    return decorator
