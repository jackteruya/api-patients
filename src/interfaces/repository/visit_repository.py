from abc import ABC, abstractmethod
from datetime import date


class VisitRepositoryInterface(ABC):
    """Interface to Visit Repository"""

    @abstractmethod
    def get_by_id(self, id: int):
        """abstractmethod"""
        raise Exception("Method not implemented")

    @abstractmethod
    def get_by_patient_id(self, patient_id: int):
        """abstractmethod"""
        raise Exception("Method not implemented")

    @abstractmethod
    def create_visit(self, patient_id: int, visit_date: date, summary: str):
        """abstractmethod"""
        raise Exception("Method not implemented")
