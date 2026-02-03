from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.extensions import db
from app.models.animal import Animal
# from flask_jwt_extended import jwt_required  # temporarily commented out for dev
# from app.utils.roles import role_required  # temporarily commented out for dev

animal_bp = Blueprint('animal', __name__, url_prefix='/api/animals')


# ----------------------------
# ADD ANIMAL (for now, keep JWT optional)
# ----------------------------
# @jwt_required()
# @role_required("owner")
@animal_bp.route("/", methods=["POST"])
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


# ----------------------------
# GET ANIMALS (no auth for dev)
# ----------------------------
# @jwt_required()
@animal_bp.route("/", methods=["GET"])
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
            "is_pregnant": animal.is_pregnant,
            "status": animal.status,
            "health_status": animal.health_status,
            "weight": animal.weight,
            "location": animal.location,
            "last_vaccination_date": animal.last_vaccination_date,
            "next_vaccination_date": animal.next_vaccination_date,
            
        })

    return jsonify(result), 200


# ----------------------------
# UPDATE ANIMAL
# ----------------------------
# @jwt_required()
# @role_required("manager")
@animal_bp.route("/<int:id>", methods=["PUT"])
def update_animal(id):
    animal = Animal.query.get_or_404(id)
    data = request.get_json()

    animal.breed = data.get("breed", animal.breed)
    animal.sex = data.get("sex", animal.sex)
    animal.is_pregnant = data.get("is_pregnant", animal.is_pregnant)

    db.session.commit()

    return jsonify({"message": "Animal updated"}), 200


# ----------------------------
# DELETE ANIMAL
# ----------------------------
# @jwt_required()
# @role_required("owner")
@animal_bp.route("/<int:id>", methods=["DELETE"])
def delete_animal(id):
    animal = Animal.query.get_or_404(id)
    db.session.delete(animal)
    db.session.commit()

    return jsonify({"message": "Animal deleted successfully"}), 200


# ----------------------------
# ANIMAL COUNTS
# ----------------------------
# @jwt_required()
@animal_bp.route("/counts", methods=["GET"])
def animal_counts():
    return jsonify({
        "cows": Animal.query.filter_by(species="cow").count(),
        "goats": Animal.query.filter_by(species="goat").count(),
        "sheep": Animal.query.filter_by(species="sheep").count()
    }), 200

@animal_bp.route("/stats", methods=["GET"])
@jwt_required()
def animal_stats():
    total = Animal.query.count()
    pregnant = Animal.query.filter_by(is_pregnant=True).count()
    healthy = Animal.query.filter_by(health_status="healthy").count()

    return jsonify({
        "total_animals": total,
        "pregnant": pregnant,
        "healthy": healthy
    }), 200