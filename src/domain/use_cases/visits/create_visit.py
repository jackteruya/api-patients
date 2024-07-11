from src.interfaces.repository.visit_repository import VisitRepositoryInterface
from src.response import ResponseFailure, ResponseTypes, ResponseSuccess


class CreateVisitUseCase:

    def __init__(self, repository: VisitRepositoryInterface) -> None:
        self._repository = repository

    def execute(self, data):
        try:
            visit = self._repository.create_visit(
                patient_id=data.patient_id,
                visit_date=data.visit_date,
                summary=data.summary
            )
            if not visit:
                return ResponseFailure(ResponseTypes.PARAMETERS_ERROR, 'Not Insert')
            return ResponseSuccess(visit)
        except Exception as ex:
            return ResponseFailure(ResponseTypes.SYSTEM_ERROR, 'System Error')
