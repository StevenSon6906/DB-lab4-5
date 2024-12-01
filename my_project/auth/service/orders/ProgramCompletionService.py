from typing import List
from my_project.auth.dao import ProgramCompletionDAO
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.ProgramCompletion import ProgramCompletion

class ProgramCompletionService(GeneralService):
    _dao = ProgramCompletionDAO

    def create(self, completion: ProgramCompletion) -> None:
        self._dao.create(completion)

    def get_all_completions(self) -> List[ProgramCompletion]:
        return self._dao.find_all()

    def get_completions_by_visitor_program_id(self, visitor_program_id: int) -> List[ProgramCompletion]:
        return self._dao.find_by_visitor_program_id(visitor_program_id)