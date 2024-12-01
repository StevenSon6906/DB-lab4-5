from typing import List
from my_project.auth.dao.orders.VisitorsDAO import VisitorsDAO
from my_project.auth.domain.orders.Visitor import Visitor

class VisitorsController:
    _dao = VisitorsDAO()

    def find_all(self) -> List[Visitor]:
        return self._dao.find_all()

    def create(self, visitor: Visitor) -> None:
        self._dao.create(visitor)

    def find_by_id(self, visitor_id: int) -> Visitor:
        return self._dao.find_by_id(visitor_id)

    def update(self, visitor_id: int, visitor: Visitor) -> None:
        self._dao.update(visitor_id, visitor)

    def delete(self, visitor_id: int) -> None:
        self._dao.delete(visitor_id)