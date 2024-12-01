from typing import List
from my_project.auth.dao.orders.VisitorProgramsDAO import VisitorProgramsDAO
from my_project.auth.domain.orders.VisitorProgram import VisitorProgram

class VisitorProgramsController:
    _dao = VisitorProgramsDAO()

    def find_all(self) -> List[VisitorProgram]:
        return self._dao.find_all()

    def create(self, visitor_program: VisitorProgram) -> None:
        self._dao.create(visitor_program)

    def find_by_id(self, visitor_program_id: int) -> VisitorProgram:
        return self._dao.find_by_id(visitor_program_id)

    def update(self, visitor_program_id: int, visitor_program: VisitorProgram) -> None:
        self._dao.update(visitor_program_id, visitor_program)

    def delete(self, visitor_program_id: int) -> None:
        self._dao.delete(visitor_program_id)