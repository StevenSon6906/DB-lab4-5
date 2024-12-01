from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Trainer import Trainer  # Ensure this is the correct path

from sqlalchemy.orm import joinedload

class TrainersDAO(GeneralDAO):
    _domain_type = Trainer

    def create(self, trainer: Trainer) -> None:
        self._session.add(trainer)
        self._session.commit()

    def find_all(self) -> List[Trainer]:
        return self._session.query(Trainer).all()

    def find_by_email(self, email: str) -> Optional[Trainer]:
        return self._session.query(Trainer).filter(Trainer.email == email).first()



    def find_with_gender(self):
        return (
            self._session.query(Trainer)
            .options(
                joinedload(Trainer.gender_info),
            )
            .all()
        )