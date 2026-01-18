from datetime import timedelta, date
from app.models.breeding import Breeding
from app.models.alert import Alert
from app.extensions import db

def schedule_pregnancy_alerts():
    today = date.today()
    breedings = Breeding.query.filter_by(status='pregnant').all()

    for breeding in breedings:
        expected = breeding.expected_birth_date
        # Trigger alerts 14, 7, 3 days before
        for days in [14, 7, 3]:
            trigger = expected - timedelta(days=days)
            if trigger >= today:
                message = f"Pregnancy alert: {breeding.female.tag_number} due in {days} days"
                alert = Alert(type='pregnancy', message=message, trigger_date=trigger)
                db.session.add(alert)
    db.session.commit()
