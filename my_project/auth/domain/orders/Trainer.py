from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto
from my_project.auth.domain.orders.Gender import Gender  # Import Gender model for relationship

class Trainer(db.Model, IDto):
    __tablename__ = "trainers"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    phone = db.Column(db.String(15))
    gender = db.Column(db.Integer)  # Foreign key column

    # Relationship with Gender, distinct from gender_id column
    # gender_info = db.relationship('Gender', back_populates="trainers")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone": self.phone,
            "gender": self.gender,
        }

    def put_into_large_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone": self.phone,
            "gender_info": self.gender_info.put_into_dto() if self.gender_info else None,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Trainer:
        return Trainer(**dto_dict)