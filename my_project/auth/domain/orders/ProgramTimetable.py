from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class ProgramTimetable(db.Model, IDto):
    __tablename__ = "programs_timetable"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    program_id = db.Column(db.Integer, db.ForeignKey('programs.id'))
    time = db.Column(db.DateTime, nullable=False)

    def put_into_dto(self) -> Dict[str, Any]:
        return {"id": self.id, "program_id": self.program_id, "time": self.time}

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ProgramTimetable:
        return ProgramTimetable(**dto_dict)