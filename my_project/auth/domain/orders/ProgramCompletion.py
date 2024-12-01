from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class ProgramCompletion(db.Model, IDto):
    __tablename__ = "program_completion"
    completion_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    visitor_program_id = db.Column(db.Integer, db.ForeignKey('visitor_programs.id'), nullable=False)
    completion_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(50), nullable=False)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "completion_id": self.completion_id,
            "visitor_program_id": self.visitor_program_id,
            "completion_date": self.completion_date,
            "status": self.status,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ProgramCompletion:
        return ProgramCompletion(**dto_dict)