from typing import Annotated

from fastapi import APIRouter, HTTPException

from src.application.schemas.patient import PatientCreateEditSchema, PatientSchema, DataPatientsSchema
from src.domain.use_cases.patients import CreatePatientUseCase, ListPatientUseCase, EditPatientUseCase
from src.infra.db.repository import PatientRepository, VisitRepository
from src.infra.db.settings import DBConnectionHandler

patient_route: APIRouter = APIRouter(prefix="/api/v1/patients")


list_ = []


@patient_route.get('', response_model=DataPatientsSchema)
def list_patients(page: int | None = 1, limit: int | None = 5):
    use_case = ListPatientUseCase(
        PatientRepository(DBConnectionHandler),
        VisitRepository(DBConnectionHandler)
    )
    result = use_case.execute(page, limit)
    return DataPatientsSchema(data=result.value, page=result.offset, limit=result.limit, count=result.count)


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
    use_case = EditPatientUseCase(PatientRepository(DBConnectionHandler))
    result = use_case.execute(id, patient)
    return PatientSchema(
        id=result.value.id,
        name=result.value.name,
        birth_date=result.value.birth_date.strftime('%y-%m-%d'),
        address=result.value.address,
        phone=result.value.phone,
        email=result.value.email,
        medical_history=result.value.medical_history
    ).model_dump()

