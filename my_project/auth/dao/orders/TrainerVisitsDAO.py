from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.TrainerVisit import TrainerVisit  # Ensure this is the correct path


class TrainerVisitsDAO(GeneralDAO):
    _domain_type = TrainerVisit

    def create(self, visit: TrainerVisit) -> None:
        self._session.add(visit)
        self._session.commit()

    def find_all(self) -> List[TrainerVisit]:
        return self._session.query(TrainerVisit).all()

    def find_by_trainer_id(self, trainer_id: int) -> List[TrainerVisit]:
        return self._session.query(TrainerVisit).filter(TrainerVisit.trainer_id == trainer_id).all()