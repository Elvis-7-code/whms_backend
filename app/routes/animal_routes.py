from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.extensions import db
from app.models.animal import Animal
from app.utils.roles import role_required

class AnimalRoutes:
    animal_bp = Blueprint('animal',__name__)

@jwt_required()
@role_required("owner")
def add_animal():
    data = request.get_json()

    if Animal.query.filter_by(tag_number=data["tag_number"]).first():
        return jsonify({"error": "Animal already exists"}), 400

    animal = Animal(
        tag_number=data["tag_number"],
        species=data["species"],
        breed=data.get("breed"),
        sex=data.get("sex"),
        date_bought=data.get("date_bought")
    )

    db.session.add(animal)
    db.session.commit()

    return jsonify({"message": "Animal added successfully"}), 201


