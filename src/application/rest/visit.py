from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


visit_route: APIRouter = APIRouter(prefix="/api/v1/visits")


list_ = []


class VisitCreate(BaseModel):
    patient_id: int
    visit_date: str
    summary: str


class VisitLis(BaseModel):
    id: int
    patient_id: int
    visit_date: str
    summary: str


@visit_route.post('')
def create_visits(visit: VisitCreate):
    data = visit.model_dump()
    data['id'] = len(list_) + 1
    list_.append(data)
    return VisitLis(**data).model_dump()


@visit_route.get('')
def list_visits():
    return {'data': list_}
