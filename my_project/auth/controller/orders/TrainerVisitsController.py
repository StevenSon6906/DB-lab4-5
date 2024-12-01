from typing import List
from my_project.auth.dao.orders.TrainerVisitsDAO import TrainerVisitsDAO
from my_project.auth.domain.orders.TrainerVisit import TrainerVisit

class TrainerVisitsController:
    _dao = TrainerVisitsDAO()

    def find_all(self) -> List[TrainerVisit]:
        return self._dao.find_all()

    def create(self, visit: TrainerVisit) -> None:
        self._dao.create(visit)

    def find_by_id(self, visit_id: int) -> TrainerVisit:
        return self._dao.find_by_id(visit_id)

    def update(self, visit_id: int, visit: TrainerVisit) -> None:
        self._dao.update(visit_id, visit)

    def delete(self, visit_id: int) -> None:
        self._dao.delete(visit_id)