from datetime import date, timedelta
from app.extensions import db
from app.models.animal import Animal
from app.models.breeding import Breeding

GESTATION_DAYS = {
    "cow": 283,
    "sheep": 150,
    "goat": 150
}

def create_breeding(male_id, female_id):
    male = Animal.query.get(male_id)
    female = Animal.query.get(female_id)

    if not male or not female:
        return {"error": "Animal not found"}, 404

    if male.sex != "male" or female.sex != "female":
        return {"error": "Invalid breeding sexes"}, 400

    if male.species != female.species:
        return {"error": "Species mismatch"}, 400

    if female.is_pregnant:
        return {"error": "Female is already pregnant"}, 400

    gestation = GESTATION_DAYS.get(female.species)
    if not gestation:
        return {"error": "Unsupported species"}, 400

    start_date = date.today()
    expected_birth = start_date + timedelta(days=gestation)

    breeding = Breeding(
        male_id=male.id,
        female_id=female.id,
        start_date=start_date,
        expected_birth_date=expected_birth,
        status="pregnant"
    )

    female.is_pregnant = True

    db.session.add(breeding)
    db.session.commit()

    return {
        "message": "Breeding recorded successfully",
        "expected_birth_date": expected_birth.isoformat()
    }, 201
