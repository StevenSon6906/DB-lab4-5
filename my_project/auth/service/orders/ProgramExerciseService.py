from typing import List
from my_project.auth.dao import ProgramExercisesDAO
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.ProgramExercise import ProgramExercise

class ProgramExerciseService(GeneralService):
    _dao = ProgramExercisesDAO

    def create(self, program_exercise: ProgramExercise) -> None:
        self._dao.create(program_exercise)

    def get_all_program_exercises(self) -> List[ProgramExercise]:
        return self._dao.find_all()

    def get_exercises_by_program_id(self, program_id: int) -> List[ProgramExercise]:
        return self._dao.find_by_program_id(program_id)