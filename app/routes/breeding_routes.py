from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import timedelta, date
from app.models.breeding import Breeding
from app.models.animal import Animal
from app.extensions import db

breeding_bp = Blueprint('breeding', __name__)

GESTATION_PERIODS = {
    'cow': 283,
    'sheep': 150,
    'goat': 150,
}

@breeding_bp.route('/breedings', methods=['POST'])
@jwt_required()
def start_breeding():
    data = request.get_json()
    male_id = data.get('male_id')
    female_id = data.get('female_id')
    start_date = data.today()

    male = Animal.query.get(male_id)
    female = Animal.query.get(female_id)

    if not male or not female:
        return jsonify({'error': 'Invalid animal IDs'}), 400

    if male.species != female.species:
        return jsonify({'error': 'Animals must be of the same species'}), 400

    gestation_days = GESTATION_PERIODS.get(female.species.lower(), 150)
    expected_birth = start_date + timedelta(days=gestation_days)

# Create Breeding record
    breeding = Breeding(
        male_id=male.id,
        female_id=female.id,
        start_date=start_date,
        expected_birth=expected_birth
    )

    female.is_pregnant = True

    db.session.add(breeding)
    db.session.commit()

    return jsonify({
        'message': 'Breeding started successfully',
        'female': female.tag_number,
        'male': male.tag_number,
        'expected_birth_date': str(expected_birth)
        }), 201