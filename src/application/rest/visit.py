from fastapi import APIRouter, status, HTTPException

from src.application.schemas import VisitSchema, VisitCreateEditSchema, DataVisitsSchema
from src.application.utils import STATUS_CODES
from src.domain.use_cases.visits import CreateVisitUseCase
from src.infra.db.repository import VisitRepository
from src.infra.db.settings import DBConnectionHandler
from src.response import ResponseTypes

visit_route: APIRouter = APIRouter(prefix="/api/v1/visits")


@visit_route.post('', status_code=status.HTTP_201_CREATED, response_model=VisitSchema)
def create_visits(visit: VisitCreateEditSchema):
    user_case = CreateVisitUseCase(VisitRepository(DBConnectionHandler))
    result = user_case.execute(visit)
    if result.type != ResponseTypes.SUCCESS:
        raise HTTPException(status_code=STATUS_CODES[result.type], detail=result.message)
    return VisitSchema(
        id=result.value.id,
        patient_id=result.value.patient_id,
        visit_date=result.value.visit_date,
        summary=result.value.summary,
    ).model_dump()
