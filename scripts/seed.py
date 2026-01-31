from datetime import date
from app import create_app
from app.extensions import db
from app.models.animal import Animal

def seed_animals():
    animals = [
        {
            "tag_number": "SHEEP-001",
            "species": "sheep",
            "breed": "Dorper",
            "sex": "female",
            "date_of_birth": date(2025, 1, 24),
            "is_pregnant": True
        },
        {
            "tag_number": "COW-001",
            "species": "cow",
            "breed": "Friesian",
            "sex": "female",
            "date_bought": date(2024, 6, 15),
            "is_pregnant": True
        },
        {
            "tag_number": "BULL-001",
            "species": "bull",
            "breed": "Boran",
            "sex": "male",
            "date_bought": date(2024, 5, 20),
            "is_pregnant": False
        },
        {
            "tag_number": "GOAT-001",
            "species": "goat",
            "breed": "Galla",
            "sex": "female",
            "date_bought": date(2024, 7, 10),
            "is_pregnant": False
        }
    ]

    for data in animals:
        exists = Animal.query.filter_by(tag_number=data["tag_number"]).first()
        if exists:
            print(f"⚠️ {data['tag_number']} already exists, skipping")
            continue

        animal = Animal(**data)
        db.session.add(animal)

    db.session.commit()
    print("✅ Animals seeded successfully")


if __name__ == "__main__":
    app = create_app()

    with app.app_context():
        # ⚠️ ONLY UNCOMMENT IF YOU INTENTIONALLY WANT TO RESET DB
        # db.drop_all()
        # db.create_all()

        seed_animals()
