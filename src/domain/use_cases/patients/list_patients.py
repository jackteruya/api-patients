from datetime import date

from src.interfaces.repository import PatientRepositoryInterface, VisitRepositoryInterface
from src.response import ResponseFailure, ResponseTypes, ResponseListSuccess


class ListPatientUseCase:

    def __init__(
            self, patient_repository: PatientRepositoryInterface, visit_repository: VisitRepositoryInterface
    ) -> None:
        self._patient_repository = patient_repository
        self._visit_repository = visit_repository

    def execute(self, offset=0, limit=5):
        try:
            offset_ = 0 if offset in [0, 1] else limit*offset-1
            patients = self._patient_repository.list_patients(limit, offset_)
            if not patients:
                return ResponseFailure(ResponseTypes.PARAMETERS_ERROR, 'Not Found')
            patients = [self._validate_patient(patient) for patient in patients]
            count_patients = self._patient_repository.count_patients()
            return ResponseListSuccess(patients, limit, offset, count_patients)
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
