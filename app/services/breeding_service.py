from datetime import timedelta
from app.models.breeding import Breeding
from app.extensions import db

Gestation_DAYS = 283

def start_breeding(female_id, male_id, start_date):
    expected_birth = start_date + timedelta(days=GESTATION_DAYS)

    breeding = Breeding(
        female_id=female_id,
        male_id=male_id,
        start_date=start_date,
        expected_birth_date=expected_birth
        status="pregnant"
    )

    db.session.add(breeding)
    db.session.commit()
    return breeding