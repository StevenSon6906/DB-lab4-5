from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

from sqlalchemy.orm import relationship

class Program(db.Model, IDto):
    __tablename__ = "programs"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

    program_exercises = relationship("ProgramExercise", back_populates="program")

    def put_into_dto(self) -> Dict[str, Any]:
        return {"id": self.id, "name": self.name, "description": self.description}

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Program:
        return Program(**dto_dict)