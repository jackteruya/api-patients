from datetime import date
from sqlalchemy import String, Date, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from src.infra.db.settings import Base


class Visits(Base):

    __tablename__ = "visits"

    id: Mapped[int] = mapped_column(primary_key=True)
    patient_id: Mapped[int] = mapped_column(ForeignKey('patients.id'))
    visit_date: Mapped[date] = mapped_column(Date)
    summary: Mapped[str] = mapped_column(String(128))

    def __repr__(self) -> str:
        return f"Visits(id={self.id!r}, patient_id={self.patient_id!r})"
