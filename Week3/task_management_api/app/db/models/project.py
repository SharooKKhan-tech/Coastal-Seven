from sqlalchemy import Integer, String
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from app.db.models.base import Base


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(100)
    )

    description: Mapped[str] = mapped_column(
        String(500)
    )

    tasks = relationship(
        "Task",
        back_populates="project"
    )