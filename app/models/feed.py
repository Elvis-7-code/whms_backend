from app.extensions import db

class Feed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feed_type = db.Column(db.String(50))
    quantity_kg = db.Column(db.Float)
    daily_usage_kg = db.Column(db.Float)
from app.extensions import db

class Feed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feed_type = db.Column(db.String(50))
    quantity_kg = db.Column(db.Float)
    daily_usage_kg = db.Column(db.Float)
