from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class Visitor(db.Model, IDto):
    __tablename__ = "visitors"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    phone = db.Column(db.String(15))
    registration_date = db.Column(db.Date)
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainers.id'))
    gender_id = db.Column(db.Integer, db.ForeignKey('gender.id'))

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone": self.phone,
            "registration_date": self.registration_date,
            "trainer_id": self.trainer_id,
            "gender_id": self.gender_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Visitor:
        return Visitor(**dto_dict)