from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Visitor import Visitor  # Ensure this is the correct path

class VisitorsDAO(GeneralDAO):
    _domain_type = Visitor

    def create(self, visitor: Visitor) -> None:
        self._session.add(visitor)
        self._session.commit()

    def find_all(self) -> List[Visitor]:
        return self._session.query(Visitor).all()

    def find_by_email(self, email: str) -> Optional[Visitor]:
        return self._session.query(Visitor).filter(Visitor.email == email).first()