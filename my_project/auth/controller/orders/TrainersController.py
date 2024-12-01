from typing import List
from my_project.auth.dao.orders.TrainersDAO import TrainersDAO
from my_project.auth.domain.orders.Trainer import Trainer

class TrainersController:
    _dao = TrainersDAO()

    def find_all(self) -> List[Trainer]:
        return self._dao.find_all()

    def create(self, trainer: Trainer) -> None:
        self._dao.create(trainer)

    def find_by_id(self, trainer_id: int) -> Trainer:
        return self._dao.find_by_id(trainer_id)

    def update(self, trainer_id: int, trainer: Trainer) -> None:
        self._dao.update(trainer_id, trainer)

    def delete(self, trainer_id: int) -> None:
        self._dao.delete(trainer_id)



    def find_with_gender(self):
        return self._dao.find_with_gender()