from datetime import date
from typing import Optional, List

from pydantic import BaseModel


class VisitCreateEditSchema(BaseModel):
    patient_id: int
    visit_date: date
    summary: str


class VisitSchema(BaseModel):
    id: int
    patient_id: int
    visit_date: date
    summary: str


class DataVisitsSchema(BaseModel):
    data: List[VisitSchema]
