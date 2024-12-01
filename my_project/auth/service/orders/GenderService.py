from typing import List
from my_project.auth.dao import GenderDAO
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.Gender import Gender

class GenderService(GeneralService):
    _dao = GenderDAO

    def create(self, gender: Gender) -> None:
        self._dao.create(gender)

    def get_all_genders(self) -> List[Gender]:
        return self._dao.find_all()

    def get_gender_by_name(self, name: str) -> Gender:
        return self._dao.find_by_name(name)