from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class VisitorProgram(db.Model, IDto):
    __tablename__ = "visitor_programs"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    visitor_id = db.Column(db.Integer, db.ForeignKey('visitors.id'), nullable=False)
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainers.id'))
    program_id = db.Column(db.Integer, db.ForeignKey('programs.id'), nullable=False)
    assigned_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "visitor_id": self.visitor_id,
            "trainer_id": self.trainer_id,
            "program_id": self.program_id,
            "assigned_date": self.assigned_date,
            "end_date": self.end_date,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> VisitorProgram:
        return VisitorProgram(**dto_dict)