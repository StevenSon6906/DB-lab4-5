from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class ProgramLog(db.Model, IDto):
    __tablename__ = "programs_logs"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    visitor_id = db.Column(db.Integer, db.ForeignKey('visitors.id'), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'), nullable=False)
    log_date = db.Column(db.Date, nullable=False)
    unit = db.Column(db.String(50))

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "visitor_id": self.visitor_id,
            "exercise_id": self.exercise_id,
            "log_date": self.log_date,
            "unit": self.unit,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ProgramLog:
        return ProgramLog(**dto_dict)