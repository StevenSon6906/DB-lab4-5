from typing import List
from my_project.auth.dao import ProgramsLogsDAO
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.ProgramLog import ProgramLog

class ProgramLogService(GeneralService):
    _dao = ProgramsLogsDAO

    def create(self, log: ProgramLog) -> None:
        self._dao.create(log)

    def get_all_logs(self) -> List[ProgramLog]:
        return self._dao.find_all()

    def get_logs_by_visitor_id(self, visitor_id: int) -> List[ProgramLog]:
        return self._dao.find_by_visitor_id(visitor_id)