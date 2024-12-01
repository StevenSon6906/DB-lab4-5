from typing import List
from my_project.auth.dao.orders.ProgramCompletionDAO import ProgramCompletionDAO
from my_project.auth.domain.orders.ProgramCompletion import ProgramCompletion

class ProgramCompletionController:
    _dao = ProgramCompletionDAO()

    def find_all(self) -> List[ProgramCompletion]:
        return self._dao.find_all()

    def create(self, completion: ProgramCompletion) -> None:
        self._dao.create(completion)

    def find_by_id(self, completion_id: int) -> ProgramCompletion:
        return self._dao.find_by_id(completion_id)

    def update(self, completion_id: int, completion: ProgramCompletion) -> None:
        self._dao.update(completion_id, completion)

    def delete(self, completion_id: int) -> None:
        self._dao.delete(completion_id)