from fastapi import APIRouter, HTTPException

from src.application.schemas import VisitSchema, VisitCreateEditSchema, DataVisitsSchema
from src.domain.use_cases.visits import CreateVisitUseCase
from src.infra.db.repository import VisitRepository
from src.infra.db.settings import DBConnectionHandler

visit_route: APIRouter = APIRouter(prefix="/api/v1/visits")


list_ = []


@visit_route.post('', response_model=VisitSchema)
def create_visits(visit: VisitCreateEditSchema):
    user_case = CreateVisitUseCase(VisitRepository(DBConnectionHandler))
    result = user_case.execute(visit)
    return VisitSchema(
        id=result.value.id,
        patient_id=result.value.patient_id,
        visit_date=result.value.visit_date,
        summary=result.value.summary,
    ).model_dump()


@visit_route.get('', response_model=DataVisitsSchema)
def list_visits():
    return {'data': list_}
