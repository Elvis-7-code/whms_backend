from app.extensions import db
from datetime import datetime

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag_number = db.Column(db.String(50), unique=True, nullable=False)
    species = db.Column(db.String(20))  # cow, bull, sheep, goat
    breed = db.Column(db.String(100))
    sex = db.Column(db.String(10))  # male, female
    date_bought = db.Column(db.Date)
    is_pregnant = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
