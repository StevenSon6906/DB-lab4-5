from typing import List
from my_project.auth.dao.orders.ProgramExercisesDAO import ProgramExercisesDAO
from my_project.auth.domain.orders.ProgramExercise import ProgramExercise

class ProgramExercisesController:
    _dao = ProgramExercisesDAO()

    def find_all(self) -> List[ProgramExercise]:
        return self._dao.find_all()

    def create(self, program_exercise: ProgramExercise) -> None:
        self._dao.create(program_exercise)

    def find_by_id(self, program_exercise_id: int) -> ProgramExercise:
        return self._dao.find_by_id(program_exercise_id)

    def update(self, program_exercise_id: int, program_exercise: ProgramExercise) -> None:
        self._dao.update(program_exercise_id, program_exercise)

    def delete(self, program_exercise_id: int) -> None:
        self._dao.delete(program_exercise_id)


    def find_all_with_related_data(self):
        return self._dao.find_all_with_related_data()
