from app.extensions import db
from datetime import date, datetime

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag_number = db.Column(db.String(50), unique=True, nullable=False)
    species = db.Column(db.String(20), nullable=False)  # cow, bull, sheep, goat
    breed = db.Column(db.String(100))
    sex = db.Column(db.String(10), nullable=False)  # male, female
    date_bought = db.Column(db.Date)
    date_of_birth = db.Column(db.Date, default=date.today)
    is_pregnant = db.Column(db.Boolean, default=False)
    status = db.Column(db.String(30), default = "active")
    health_status = db.Column(db.String(30), default = "healthy")
    weight = db.Column(db.Float, nullable=True)
    daily_feed_kg = db.Column(db.Float, nullable=True)
    rfid_tag = db.Column(db.String(100), unique=True, nullable=True)
    location = db.Column(db.String(100), nullable=True)

    last_vaccination_date = db.Column(db.Date, nullable=True)
    next_vaccination_date = db.Column(db.Date, nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
