from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.VisitorProgram import VisitorProgram  # Ensure this is the correct path


class VisitorProgramsDAO(GeneralDAO):
    _domain_type = VisitorProgram

    def create(self, visitor_program: VisitorProgram) -> None:
        self._session.add(visitor_program)
        self._session.commit()

    def find_all(self) -> List[VisitorProgram]:
        return self._session.query(VisitorProgram).all()

    def find_by_visitor_id(self, visitor_id: int) -> List[VisitorProgram]:
        return self._session.query(VisitorProgram).filter(VisitorProgram.visitor_id == visitor_id).all()