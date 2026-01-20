from app.models.alert import Alert 
from app.extensions import db

def create_alert (alert_type, message, trigger_date):
    alert = Alert(
        type=alert_type,
        message=message,
        trigger_date=trigger_date
    )
    db.session.add(alert)
    db.session.commit()
    return alert