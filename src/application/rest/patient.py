from fastapi import APIRouter, HTTPException

from src.application.schemas.patient import PatientCreateEditSchema, PatientSchema, DataPatientsSchema

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
    data = patient.model_dump()
    data['id'] = len(list_) + 1
    list_.append(data)
    return PatientSchema(**data).model_dump()


@patient_route.put('/{id}', response_model=PatientSchema)
def edit_patients(id: int, patient: PatientCreateEditSchema):
    data = patient.model_dump()
    data['id'] = id
    list_[id-1] = data
    return PatientSchema(**data).model_dump()

