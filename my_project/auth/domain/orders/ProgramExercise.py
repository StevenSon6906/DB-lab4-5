from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

from sqlalchemy.orm import backref
from sqlalchemy.orm import relationship


class ProgramExercise(db.Model, IDto):
    __tablename__ = "program_exercises"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    program_id = db.Column(db.Integer, db.ForeignKey('programs.id'), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'), nullable=False)
    target_value = db.Column(db.Integer, nullable=False)

    program = relationship("Program", back_populates="program_exercises")
    exercise = relationship("Exercise", back_populates="program_exercises")

    def put_into_large_dto(self) -> Dict[str, Any]:
        return {
            "program_exercise": {
                "program_id": self.program_id,
                "exercise_id": self.exercise_id,
                "target_value": self.target_value
            },
            "program": {
                "id": self.program.id,
                "name": self.program.name,
                "description": self.program.description
            } if self.program else None,
            "exercise": {
                "id": self.exercise.id,
                "name": self.exercise.name,
                "description": self.exercise.description,
                "unit": self.exercise.unit
            } if self.exercise else None
        }

    def put_into_dto(self) -> Dict[str, Any]:
        return {"id": self.id, "program_id": self.program_id, "exercise_id": self.exercise_id, "target_value": self.target_value}

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ProgramExercise:
        return ProgramExercise(**dto_dict)