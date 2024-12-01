from typing import List
from my_project.auth.dao import TrainerVisitsDAO
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.TrainerVisit import TrainerVisit

class TrainerVisitService(GeneralService):
    _dao = TrainerVisitsDAO

    def create(self, visit: TrainerVisit) -> None:
        self._dao.create(visit)

    def get_all_trainer_visits(self) -> List[TrainerVisit]:
        return self._dao.find_all()

    def get_visits_by_trainer_id(self, trainer_id: int) -> List[TrainerVisit]:
        return self._dao.find_by_trainer_id(trainer_id)