from typing import List
from my_project.auth.dao import VisitorsDAO
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.Visitor import Visitor

class VisitorService(GeneralService):
    _dao = VisitorsDAO

    def create(self, visitor: Visitor) -> None:
        self._dao.create(visitor)

    def get_all_visitors(self) -> List[Visitor]:
        return self._dao.find_all()

    def get_visitor_by_email(self, email: str) -> Visitor:
        return self._dao.find_by_email(email)