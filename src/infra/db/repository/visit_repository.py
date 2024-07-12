from datetime import date

from sqlalchemy import desc

from src.infra.db.entities import Visits
from src.interfaces.repository import VisitRepositoryInterface


class VisitRepository(VisitRepositoryInterface):

    def __init__(self, db_connection):
        self.__db_connection = db_connection

    def get_by_id(self, id: int):
        try:
            with self.__db_connection() as db_connection:
                visit = db_connection.session.query(Visits).filter_by(id=id).first()
                return visit
        except Exception as ex:
            raise None

    def get_by_patient_id(self, patient_id: int):
        try:
            with self.__db_connection() as db_connection:
                visit = db_connection.session.query(Visits).filter_by(
                    patient_id=patient_id
                ).order_by(desc(Visits.visit_date)).first()
                return visit
        except Exception as ex:
            return None

    def create_visit(self, patient_id: int, visit_date: date, summary: str):
        try:
            with self.__db_connection() as db_connection:
                new_visit = Visits(
                    patient_id=patient_id,
                    visit_date=visit_date,
                    summary=summary,
                )
                db_connection.session.add(new_visit)
                db_connection.session.commit()
                db_connection.session.refresh(new_visit)
                return new_visit
        except Exception as ex:
            return None
