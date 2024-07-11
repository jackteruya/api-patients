from src.interfaces.repository.patient_repository import PatientRepositoryInterface
from src.response import ResponseFailure, ResponseTypes, ResponseSuccess


class CreatePatientUseCase:

    def __init__(self, repository: PatientRepositoryInterface) -> None:
        self._repository = repository

    def execute(self, data):
        try:
            patient = self._repository.create_patient(
                name=data.name,
                birth_date=data.birth_date,
                address=data.address,
                phone=data.phone,
                email=data.email,
                medical_history=data.medical_history,
            )
            if not patient:
                return ResponseFailure(ResponseTypes.PARAMETERS_ERROR, 'Not Insert')
            return ResponseSuccess(patient)
        except Exception as ex:
            return ResponseFailure(ResponseTypes.SYSTEM_ERROR, 'System Error')
