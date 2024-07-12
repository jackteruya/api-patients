from typing import Annotated

from fastapi import APIRouter, HTTPException, status

from src.application.schemas.patient import PatientCreateEditSchema, PatientSchema, DataPatientsSchema
from src.application.utils import STATUS_CODES
from src.domain.use_cases.patients import CreatePatientUseCase, ListPatientUseCase, EditPatientUseCase
from src.infra.db.repository import PatientRepository, VisitRepository
from src.infra.db.settings import DBConnectionHandler
from src.response import ResponseTypes

patient_route: APIRouter = APIRouter(prefix="/api/v1/patients")


list_ = []


@patient_route.get('', status_code=status.HTTP_200_OK, response_model=DataPatientsSchema)
def list_patients(page: int | None = 1, limit: int | None = 5):
    use_case = ListPatientUseCase(
        PatientRepository(DBConnectionHandler),
        VisitRepository(DBConnectionHandler)
    )
    result = use_case.execute(page, limit)
    if result.type != ResponseTypes.SUCCESS:
        raise HTTPException(status_code=STATUS_CODES[result.type], detail=result.message)
    return DataPatientsSchema(data=result.value, page=result.offset, limit=result.limit, count=result.count)


@patient_route.post('', status_code=status.HTTP_201_CREATED, response_model=PatientSchema)
def create_patients(patient: PatientCreateEditSchema):
    use_case = CreatePatientUseCase(PatientRepository(DBConnectionHandler))
    result = use_case.execute(patient)
    if result.type != ResponseTypes.SUCCESS:
        raise HTTPException(status_code=STATUS_CODES[result.type], detail=result.message)
    return PatientSchema(
        id=result.value.id,
        name=result.value.name,
        birth_date=result.value.birth_date.strftime('%y-%m-%d'),
        address=result.value.address,
        phone=result.value.phone,
        email=result.value.email,
        medical_history=result.value.medical_history,
    ).model_dump()
    # return data.value


@patient_route.put('/{id}', status_code=status.HTTP_200_OK, response_model=PatientSchema)
def edit_patients(id: int, patient: PatientCreateEditSchema):
    use_case = EditPatientUseCase(PatientRepository(DBConnectionHandler))
    result = use_case.execute(id, patient)
    if result.type != ResponseTypes.SUCCESS:
        raise HTTPException(status_code=STATUS_CODES[result.type], detail=result.message)
    return PatientSchema(
        id=result.value.id,
        name=result.value.name,
        birth_date=result.value.birth_date.strftime('%y-%m-%d'),
        address=result.value.address,
        phone=result.value.phone,
        email=result.value.email,
        medical_history=result.value.medical_history
    ).model_dump()

