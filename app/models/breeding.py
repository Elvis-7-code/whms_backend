from datetime import timedelta
from app.extensions import db

class Breeding(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    male_id = db.Column(db.Integer, db.ForeignKey("animal.id"), nullable=False)
    female_id = db.Column(db.Integer, db.ForeignKey("animal.id"), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=True)
    expected_birth = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), default='pregnant')  # active, completed
