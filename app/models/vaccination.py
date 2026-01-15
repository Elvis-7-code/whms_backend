from app.extensions import db

class Vaccination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    animal_id = db.Column(db.Integer, db.ForeignKey("animal.id"))
    vaccine_name = db.Column(db.String(100))
    scheduled_date = db.Column(db.Date)
    administered = db.Column(db.Boolean, default=False)
