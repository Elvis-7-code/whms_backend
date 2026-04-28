from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.extensions import db
from app.models.animal import Animal

animal_bp = Blueprint('animal', __name__)

@animal_bp.route('', methods=['GET', 'OPTIONS'])
@jwt_required()
def get_animals():
    if request.method == 'OPTIONS':
        return jsonify({}), 200
    
    animals = Animal.query.all()
    result = [{
        "id": a.id,
        "tag_number": a.tag_number,
        "species": a.species,
        "breed": a.breed,
        "sex": a.sex,
        "is_pregnant": a.is_pregnant
    } for a in animals]
    
    return jsonify(result), 200

@animal_bp.route('', methods=['POST', 'OPTIONS'])
@jwt_required()
def add_animal():
    if request.method == 'OPTIONS':
        return jsonify({}), 200
    
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