from fastapi import APIRouter, HTTPException

from src.application.schemas import VisitSchema, VisitCreateEditSchema, DataVisitsSchema

visit_route: APIRouter = APIRouter(prefix="/api/v1/visits")


list_ = []


@visit_route.post('', response_model=VisitSchema)
def create_visits(visit: VisitCreateEditSchema):
    data = visit.model_dump()
    data['id'] = len(list_) + 1
    list_.append(data)
    return VisitSchema(**data).model_dump()


@visit_route.get('', response_model=DataVisitsSchema)
def list_visits():
    return {'data': list_}
