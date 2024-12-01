from typing import List
from my_project.auth.dao.orders.ProgramsTimetableDAO import ProgramsTimetableDAO
from my_project.auth.domain.orders.ProgramTimetable import ProgramTimetable

class ProgramsTimetableController:
    _dao = ProgramsTimetableDAO()

    def find_all(self) -> List[ProgramTimetable]:
        return self._dao.find_all()

    def create(self, timetable: ProgramTimetable) -> None:
        self._dao.create(timetable)

    def find_by_id(self, timetable_id: int) -> ProgramTimetable:
        return self._dao.find_by_id(timetable_id)

    def update(self, timetable_id: int, timetable: ProgramTimetable) -> None:
        self._dao.update(timetable_id, timetable)

    def delete(self, timetable_id: int) -> None:
        self._dao.delete(timetable_id)