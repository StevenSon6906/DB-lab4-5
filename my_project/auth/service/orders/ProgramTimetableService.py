from typing import List
from my_project.auth.dao import ProgramsTimetableDAO
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.ProgramTimetable import ProgramTimetable


class ProgramTimetableService(GeneralService):
    _dao = ProgramsTimetableDAO

    def create(self, timetable: ProgramTimetable) -> None:
        self._dao.create(timetable)

    def get_all_program_timetables(self) -> List[ProgramTimetable]:
        return self._dao.find_all()

    def get_timetable_by_program_id(self, program_id: int) -> List[ProgramTimetable]:
        return self._dao.find_by_program_id(program_id)