from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from app.models.vaccination import Vaccination
from app.extensions import db

vaccination_bp = Blueprint("vaccination", __name__, url_prefix='/vaccinations')

@vaccination_bp.route("/vaccinations", methods=["GET"]) 
def get_vaccinations():
    return jsonify({"message": "Vaccination routes working"})