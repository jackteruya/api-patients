from datetime import date

from sqlalchemy import update, select
from sqlalchemy.orm import aliased

from src.infra.db.entities import Patients, Visits
from src.interfaces.repository import PatientRepositoryInterface


class PatientRepository(PatientRepositoryInterface):

    def __init__(self, db_connection):
        self.__db_connection = db_connection

    def get_by_id(self, id: int):
        try:
            with self.__db_connection() as db_connection:
                # select(Patients).where(Patients.id == id)
                patient = db_connection.session.query(Patients).filter_by(id=id).first()
                return patient
        except Exception as ex:
            raise None

    def list_patients(self):
        try:
            with self.__db_connection() as db_connection:
                patients = db_connection.session.scalars(select(Patients)).all()
                return patients
        except Exception as ex:
            print(ex)
            raise None

    def create_patient(self, name: str, birth_date: date, address: str, phone: str, email: str, medical_history: str):
        try:
            with self.__db_connection() as db_connection:
                new_patient = Patients(
                    name=name,
                    birth_date=birth_date,
                    address=address,
                    phone=phone,
                    email=email,
                    medical_history=medical_history
                )
                db_connection.session.add(new_patient)
                db_connection.session.commit()
                db_connection.session.refresh(new_patient)
                return new_patient
        except Exception as ex:
            raise None

    def edit_patient(
            self, id: int, name: int, birth_date: date, address: str, phone: str, email: str, medical_history: str
    ):
        try:
            with self.__db_connection() as db_connection:
                patient = update(Patients).where(Patients.id == id).values(
                    name=name,
                    birth_date=birth_date,
                    address=address,
                    phone=phone,
                    email=email,
                    medical_history=medical_history
                )
                db_connection.session.execute(patient)
                db_connection.session.refresh(patient)
                return patient
        except Exception as ex:
            raise None
