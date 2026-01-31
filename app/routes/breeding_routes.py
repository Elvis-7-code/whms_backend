from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.services.breeding_service import create_breeding

breeding_bp = Blueprint("breeding", __name__, url_prefix="/breeding")

@breeding_bp.route("/", methods=["POST"])
@jwt_required()
def breed():
    data = request.get_json()

    male_id = data.get("male_id")
    female_id = data.get("female_id")

    response, status = create_breeding(male_id, female_id)
    return jsonify(response), status
