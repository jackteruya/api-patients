from src.interfaces.repository import PatientRepositoryInterface
from src.response import ResponseFailure, ResponseTypes, ResponseSuccess


class EditPatientUseCase:

    def __init__(self, patient_repository: PatientRepositoryInterface) -> None:
        self._patient_repository = patient_repository

    def execute(self, id, data):
        try:
            self._patient_repository.edit_patient(
                id=id,
                name=data.name,
                birth_date=data.birth_date,
                address=data.address,
                phone=data.phone,
                email=data.email,
                medical_history=data.medical_history
            )
            patient = self._patient_repository.get_by_id(id)

            if self.validation_patient_updated(data, patient):
                return ResponseSuccess(patient)
            return ResponseFailure(ResponseTypes.PARAMETERS_ERROR, 'Not Update')
        except Exception as ex:
            return ResponseFailure(ResponseTypes.SYSTEM_ERROR, 'System Error')

    def validation_patient_updated(self, data, patient):
        if patient.name != data.name:
            return False
        if patient.birth_date != data.birth_date:
            return False
        if patient.address != data.address:
            return False
        if patient.phone != data.phone:
            return False
        if patient.email != data.email:
            return False
        if patient.medical_history != data.medical_history:
            return False
        return True
