from typing import List
from my_project.auth.dao import programsDao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.Program import Program

#ВОНО НЕ МАТЮКАЄТЬСЯ якщо у ДАО лише одне слово, типу находить

class ProgramService(GeneralService):
    _dao = programsDao

    def create(self, program: Program) -> None:
        self._dao.create(program)

    def get_all_programs(self) -> List[Program]:
        return self._dao.find_all()

    def get_program_by_name(self, name: str) -> Program:
        return self._dao.find_by_name(name)