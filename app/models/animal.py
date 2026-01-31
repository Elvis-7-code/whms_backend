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

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
