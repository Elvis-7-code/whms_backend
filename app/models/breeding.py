from app.extensions import db

class Breeding(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bull_id = db.Column(db.Integer, db.ForeignKey("animal.id"))
    cow_id = db.Column(db.Integer, db.ForeignKey("animal.id"))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    expected_birth = db.Column(db.Date)
    status = db.Column(db.String(20))  # active, completed
