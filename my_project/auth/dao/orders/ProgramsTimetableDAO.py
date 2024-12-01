from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.ProgramTimetable import ProgramTimetable  # Ensure this is the correct path

class ProgramsTimetableDAO(GeneralDAO):
    _domain_type = ProgramTimetable

    def create(self, timetable: ProgramTimetable) -> None:
        self._session.add(timetable)
        self._session.commit()

    def find_all(self) -> List[ProgramTimetable]:
        return self._session.query(ProgramTimetable).all()

    def find_by_program_id(self, program_id: int) -> List[ProgramTimetable]:
        return self._session.query(ProgramTimetable).filter(ProgramTimetable.program_id == program_id).all()