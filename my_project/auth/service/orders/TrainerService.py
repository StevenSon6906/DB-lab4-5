from typing import List
from my_project.auth.dao import TrainersDAO
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.Trainer import Trainer

class TrainerService(GeneralService):
    _dao = TrainersDAO

    def create(self, trainer: Trainer) -> None:
        self._dao.create(trainer)

    def get_all_trainers(self) -> List[Trainer]:
        return self._dao.find_all()

    def get_trainer_by_email(self, email: str) -> Trainer:
        return self._dao.find_by_email(email)