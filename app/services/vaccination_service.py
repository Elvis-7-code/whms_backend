from app.extensions import db
from app.models.vaccination import Vaccination 

def record_vaccination(data);
    vaccination = Vaccination(**data)
    db.session.add(vaccination)
    db.session.commit()
    return vaccination