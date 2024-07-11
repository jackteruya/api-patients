from abc import ABC, abstractmethod
from datetime import date


class PatientRepositoryInterface(ABC):
    """Interface to Visit Repository"""

    @abstractmethod
    def get_by_id(self, id: int):
        """abstractmethod"""
        raise Exception("Method not implemented")

    @abstractmethod
    def list_patients(self):
        """abstractmethod"""
        raise Exception("Method not implemented")

    @abstractmethod
    def create_patient(self, name: int, birth_date: date, address: str, phone: str, email: str, medical_history: str):
        """abstractmethod"""
        raise Exception("Method not implemented")

    @abstractmethod
    def edit_patient(
            self, id: int, name: int, birth_date: date, address: str, phone: str, email: str, medical_history: str
    ):
        """abstractmethod"""
        raise Exception("Method not implemented")
