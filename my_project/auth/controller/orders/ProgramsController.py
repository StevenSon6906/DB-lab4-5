from typing import List
from my_project.auth.dao.orders.ProgramsDAO import ProgramsDAO
from my_project.auth.domain.orders.Program import Program

class ProgramsController:
    _dao = ProgramsDAO()

    def find_all(self) -> List[Program]:
        return self._dao.find_all()

    def create(self, program: Program) -> None:
        self._dao.create(program)

    def find_by_id(self, program_id: int) -> Program:
        return self._dao.find_by_id(program_id)

    def update(self, program_id: int, program: Program) -> None:
        self._dao.update(program_id, program)

    def delete(self, program_id: int) -> None:
        self._dao.delete(program_id)