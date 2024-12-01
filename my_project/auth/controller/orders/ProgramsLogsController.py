from typing import List
from my_project.auth.dao.orders.ProgramsLogsDAO import ProgramsLogsDAO
from my_project.auth.domain.orders.ProgramLog import ProgramLog

class ProgramsLogsController:
    _dao = ProgramsLogsDAO()

    def find_all(self) -> List[ProgramLog]:
        return self._dao.find_all()

    def create(self, log: ProgramLog) -> None:
        self._dao.create(log)

    def find_by_id(self, log_id: int) -> ProgramLog:
        return self._dao.find_by_id(log_id)

    def update(self, log_id: int, log: ProgramLog) -> None:
        self._dao.update(log_id, log)

    def delete(self, log_id: int) -> None:
        self._dao.delete(log_id)