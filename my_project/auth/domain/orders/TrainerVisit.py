from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class TrainerVisit(db.Model, IDto):
    __tablename__ = "trainer_visits"
    visit_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainers.id'), nullable=False)
    visitor_id = db.Column(db.Integer, db.ForeignKey('visitors.id'), nullable=False)
    visit_date = db.Column(db.Date, nullable=False)
    notes = db.Column(db.Text)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "visit_id": self.visit_id,
            "trainer_id": self.trainer_id,
            "visitor_id": self.visitor_id,
            "visit_date": self.visit_date,
            "notes": self.notes,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> TrainerVisit:
        return TrainerVisit(**dto_dict)