from flask import Blueprint, jsonify
 vaccination_bp = Blueprint("vaccination", __name__)

@vaccination_bp.route("/vaccinations", methods=["GET"]) 
def get_vaccinations():
    return jsonify({"message": "Vaccination routes working"})