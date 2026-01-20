from app.models.animal import Animal
from app.extensions import db

def create_animal(data):
    animal = Animal(**data)
    db.session.add(animal)
    db.session.commit()
    return animal

def get_all_animals():
    return Animal.query.all()