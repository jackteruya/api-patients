from datetime import date

from src.domain.entities.patients import Patient
from src.interfaces.repository import PatientRepositoryInterface, VisitRepositoryInterface
from src.response import ResponseFailure, ResponseTypes, ResponseSuccess


class ListPatientUseCase:

    def __init__(
            self, patient_repository: PatientRepositoryInterface, visit_repository: VisitRepositoryInterface
    ) -> None:
        self._patient_repository = patient_repository
        self._visit_repository = visit_repository

    def execute(self):
        try:
            patients = self._patient_repository.list_patients()
            if not patients:
                return ResponseFailure(ResponseTypes.PARAMETERS_ERROR, 'Not Insert')
            patients = [self._validate_patient(patient) for patient in patients]
            return ResponseSuccess(patients)
        except Exception as ex:
            return ResponseFailure(ResponseTypes.SYSTEM_ERROR, 'System Error')

    def _validate_patient(self, patient):
        return {
            "id": patient.id,
            "name": patient.name,
            "age": self._get_age(patient.birth_date),
            "phone": patient.phone,
            "email": patient.email,
            "last_visit_summary": self._get_last_visit_summary(patient.id)

        }

    def _get_age(self, birth_date):
        today = date.today()
        age = today.year - birth_date.year
        if today.month <= birth_date.month:
            if today.day < birth_date.day:
                age -= 1
        return age

    def _get_last_visit_summary(self, patient_id):
        visit = self._visit_repository.get_by_patient_id(patient_id)
        if visit is None:
            return "Not Visit"
        return f'Visit on {visit.visit_date}: {visit.summary}'
