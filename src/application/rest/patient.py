from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


patient_route: APIRouter = APIRouter(prefix="/api/v1/patients")


list_ = []


class PatientCreate(BaseModel):
    name: str
    birth_date: str
    address: str
    phone: str
    email: str
    medical_history: str


class PatientLis(BaseModel):
    id: Optional[int]
    name: str
    birth_date: str
    address: str
    phone: str
    email: str
    medical_history: str


@patient_route.get('')
def list_patients():
    return {'data': list_}


@patient_route.post('')
def create_patients(patient: PatientCreate):
    data = patient.model_dump()
    data['id'] = len(list_) + 1
    list_.append(data)
    return PatientLis(**data).model_dump()


@patient_route.put('/{id}')
def edit_patients(id: int, patient: PatientCreate):
    data = patient.model_dump()
    data['id'] = id
    list_[id-1] = data
    return PatientLis(**data).model_dump()

