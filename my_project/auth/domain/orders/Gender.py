from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

from sqlalchemy.orm import relationship


class Gender(db.Model, IDto):
    __tablename__ = "gender"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)

    # trainers = relationship("Trainer", back_populates="gender_info")

    def put_into_dto(self) -> Dict[str, Any]:
        return {"id": self.id, "name": self.name}

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Gender:
        return Gender(**dto_dict)

