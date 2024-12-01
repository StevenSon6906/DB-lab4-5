from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.ProgramLog import ProgramLog


class ProgramsLogsDAO(GeneralDAO):
    _domain_type = ProgramLog

    def create(self, log: ProgramLog) -> None:
        self._session.add(log)
        self._session.commit()

    def find_all(self) -> List[ProgramLog]:
        return self._session.query(ProgramLog).all()

    def find_by_visitor_id(self, visitor_id: int) -> List[ProgramLog]:
        return self._session.query(ProgramLog).filter(ProgramLog.visitor_id == visitor_id).all()