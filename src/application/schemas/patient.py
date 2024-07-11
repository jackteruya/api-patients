from datetime import date
from typing import Optional, List

from pydantic import BaseModel


class PatientCreateEditSchema(BaseModel):
    name: str
    birth_date: date
    address: str
    phone: str
    email: str
    medical_history: str


class PatientSchema(BaseModel):
    id: int
    name: str
    birth_date: str
    address: str
    phone: str
    email: str
    medical_history: str


class PatientsListSchema(BaseModel):
    id: Optional[int]
    name: str
    age: int
    phone: str
    email: str
    last_visit_summary: str


class DataPatientsSchema(BaseModel):
    data: List[PatientsListSchema]
