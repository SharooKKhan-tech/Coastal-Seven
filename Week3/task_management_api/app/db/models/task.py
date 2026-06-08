from sqlalchemy import (
    Integer,
    String,
    ForeignKey
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from app.db.models.base import Base


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    title: Mapped[str] = mapped_column(
        String(200)
    )

    description: Mapped[str] = mapped_column(
        String(500)
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="TODO"
    )

    priority: Mapped[str] = mapped_column(
        String(20),
        default="MEDIUM"
    )

    assigned_to: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    project_id: Mapped[int] = mapped_column(
        ForeignKey("projects.id")
    )

    assigned_user = relationship(
        "User",
        back_populates="tasks"
    )

    project = relationship(
        "Project",
        back_populates="tasks"
    )