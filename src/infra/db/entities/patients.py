from datetime import date
from typing import Optional, List
from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship

from src.infra.db.entities.visits import Visits
from src.infra.db.settings import Base


class Patients(Base):

    __tablename__ = "patients"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(128))
    birth_date: Mapped[date] = mapped_column(Date)
    address: Mapped[str] = mapped_column(String(128))
    phone: Mapped[str] = mapped_column(String(128))
    email: Mapped[str] = mapped_column(String(128))
    medical_history: Mapped[str] = mapped_column(String(128))

    visits: Mapped[List[Visits]] = relationship("Visits")

    def __repr__(self) -> str:
        return f"Patients(id={self.id!r}, name={self.name!r})"
