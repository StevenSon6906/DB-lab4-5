from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.ProgramCompletion import ProgramCompletion  # Ensure this is the correct path


class ProgramCompletionDAO(GeneralDAO):
    _domain_type = ProgramCompletion

    def create(self, completion: ProgramCompletion) -> None:
        self._session.add(completion)
        self._session.commit()

    def find_all(self) -> List[ProgramCompletion]:
        return self._session.query(ProgramCompletion).all()

    def find_by_visitor_program_id(self, visitor_program_id: int) -> List[ProgramCompletion]:
        return self._session.query(ProgramCompletion).filter(
            ProgramCompletion.visitor_program_id == visitor_program_id).all()