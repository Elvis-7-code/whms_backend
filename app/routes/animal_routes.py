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

@animal_bp.route("/", methods=["GET"])
@jwt_required()
def get_animals():
    animals = Animal.query.all()

    result = []
    for animal in animals:
        result.append({
            "id": animal.id,
            "tag_number": animal.tag_number,
            "species": animal.species,
            "breed": animal.breed,
            "sex": animal.sex,
            "is_pregnant": animal.is_pregnant
        })

    return jsonify(result), 200

@animal_bp.route("/<int:id>", methods=["PUT"])
@jwt_required()
@role_required("manager")
def update_animal(id):
    animal = Animal.query.get_or_404(id)
    data = request.get_json()

    animal.breed = data.get("breed", animal.breed)
    animal.sex = data.get("sex", animal.sex)
    animal.is_pregnant = data.get("is_pregnant", animal.is_pregnant)

    db.session.commit()

    return jsonify({"message": "Animal updated"}), 200
