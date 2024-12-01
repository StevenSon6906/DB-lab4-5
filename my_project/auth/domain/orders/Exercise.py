from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

from sqlalchemy.orm import relationship


class Exercise(db.Model, IDto):
    __tablename__ = "exercises"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    unit = db.Column(db.String(50))



    program_exercises = relationship("ProgramExercise", back_populates="exercise")



    def put_into_dto(self) -> Dict[str, Any]:
        return {"id": self.id, "name": self.name, "description": self.description, "unit": self.unit}

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Exercise:
        return Exercise(**dto_dict)