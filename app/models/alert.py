from app.extensions import db
from datetime import date


class Alert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50))  # feed, pregnancy, vaccination
    message = db.Column(db.Text)
    trigger_date = db.Column(db.Date)
    sent = db.Column(db.Boolean, default=False)
