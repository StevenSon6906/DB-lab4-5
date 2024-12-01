from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Program import Program  # Ensure this is the correct path


class ProgramsDAO(GeneralDAO):
    _domain_type = Program

    def create(self, program: Program) -> None:
        self._session.add(program)
        self._session.commit()

    def find_all(self) -> List[Program]:
        return self._session.query(Program).all()

    def find_by_name(self, name: str) -> Optional[Program]:
        return self._session.query(Program).filter(Program.name == name).first()