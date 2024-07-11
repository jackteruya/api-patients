from fastapi import APIRouter, HTTPException

from src.application.schemas.patient import PatientCreateEditSchema, PatientSchema, DataPatientsSchema
from src.domain.use_cases.patients import CreatePatientUseCase, ListPatientUseCase
from src.infra.db.repository import PatientRepository, VisitRepository
from src.infra.db.settings import DBConnectionHandler

patient_route: APIRouter = APIRouter(prefix="/api/v1/patients")


list_ = []


@patient_route.get('', response_model=DataPatientsSchema)
def list_patients():
    use_case = ListPatientUseCase(
        PatientRepository(DBConnectionHandler),
        VisitRepository(DBConnectionHandler)
    )
    result = use_case.execute()
    return DataPatientsSchema(data=result.value)


@patient_route.post('', response_model=PatientSchema)
def create_patients(patient: PatientCreateEditSchema):
    use_case = CreatePatientUseCase(PatientRepository(DBConnectionHandler))
    data = use_case.execute(patient)
    return PatientSchema(
        id=data.value.id,
        name=data.value.name,
        birth_date=data.value.birth_date.strftime('%y-%m-%d'),
        address=data.value.address,
        phone=data.value.phone,
        email=data.value.email,
        medical_history=data.value.medical_history,
    ).model_dump()
    # return data.value


@patient_route.put('/{id}', response_model=PatientSchema)
def edit_patients(id: int, patient: PatientCreateEditSchema):
    data = patient.model_dump()
    data['id'] = id
    list_[id-1] = data
    return PatientSchema(**data).model_dump()

