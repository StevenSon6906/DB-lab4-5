from typing import List
from my_project.auth.dao.orders.ExercisesDAO import ExercisesDAO
from my_project.auth.domain.orders.Exercise import Exercise

class ExercisesController:
    _dao = ExercisesDAO()

    def find_all(self) -> List[Exercise]:
        return self._dao.find_all()

    def create(self, exercise: Exercise) -> None:
        self._dao.create(exercise)

    def find_by_id(self, exercise_id: int) -> Exercise:
        return self._dao.find_by_id(exercise_id)

    def update(self, exercise_id: int, exercise: Exercise) -> None:
        self._dao.update(exercise_id, exercise)

    def delete(self, exercise_id: int) -> None:
        self._dao.delete(exercise_id)