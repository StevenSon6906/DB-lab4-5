from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.ProgramExercise import ProgramExercise  # Ensure this is the correct path

from sqlalchemy.orm import joinedload

class ProgramExercisesDAO(GeneralDAO):
    _domain_type = ProgramExercise

    def create(self, program_exercise: ProgramExercise) -> None:
        self._session.add(program_exercise)
        self._session.commit()

    def find_all(self) -> List[ProgramExercise]:
        return self._session.query(ProgramExercise).all()

    def find_by_program_id(self, program_id: int) -> List[ProgramExercise]:
        return self._session.query(ProgramExercise).filter(ProgramExercise.program_id == program_id).all()




    def find_all_with_related_data(self):
        return (
            self._session.query(ProgramExercise)
            .options(
                joinedload(ProgramExercise.exercise),
                joinedload(ProgramExercise.program)
            )
            .all()
        )