"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from abc import abstractmethod
from typing import Dict


class IDto:
    """
    Interface to put and extract DTO objects to/from domain objects.
    """

    @abstractmethod
    def put_into_dto(self) -> Dict[str, object]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """

    @staticmethod
    @abstractmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> object:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
