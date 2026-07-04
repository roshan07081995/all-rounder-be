from uuid import UUID
from uuid import uuid4

from datetime import date
from datetime import datetime

from sqlalchemy import Boolean
from sqlalchemy import Date
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import UniqueConstraint

from sqlalchemy.dialects.postgresql import UUID as PG_UUID

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.core.base import Base


class MonthlyTaskCompletion(Base):

    __tablename__ = "monthly_task_completions"

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "task_id",
            "completion_date",
            name="uq_monthly_task_completion_user_task_date",
        ),
    )

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    task_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("daily_tasks.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    completion_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
        index=True,
    )

    is_completed: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )
