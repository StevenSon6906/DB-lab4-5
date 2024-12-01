from typing import List
from my_project.auth.dao import VisitorProgramsDAO
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.VisitorProgram import VisitorProgram

class VisitorProgramService(GeneralService):
    _dao = VisitorProgramsDAO

    def create(self, visitor_program: VisitorProgram) -> None:
        self._dao.create(visitor_program)

    def get_all_visitor_programs(self) -> List[VisitorProgram]:
        return self._dao.find_all()

    def get_programs_by_visitor_id(self, visitor_id: int) -> List[VisitorProgram]:
        return self._dao.find_by_visitor_id(visitor_id)