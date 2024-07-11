from fastapi import APIRouter, HTTPException

from src.application.schemas.patient import PatientCreateEditSchema, PatientSchema, DataPatientsSchema
from src.domain.use_cases.patients import CreatePatientUseCase
from src.infra.db.repository import PatientRepository
from src.infra.db.settings import DBConnectionHandler

patient_route: APIRouter = APIRouter(prefix="/api/v1/patients")


list_ = []


@patient_route.get('', response_model=DataPatientsSchema)
def list_patients():
    data = []
    for d in list_:
        data.append({
            "id": d['id'],
            "name": d['name'],
            "age": int(d['birth_date'][-2:]),
            "phone": d['phone'],
            "email": d['email'],
            "last_visit_summary": d['medical_history']
        })
    return {'data': data}


@patient_route.post('', response_model=PatientSchema)
def create_patients(patient: PatientCreateEditSchema):
    use_case = CreatePatientUseCase(PatientRepository(DBConnectionHandler))
    data = use_case.execute(patient)
    list_.append(data.value)
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

