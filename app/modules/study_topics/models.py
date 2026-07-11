from uuid import UUID
from uuid import uuid4

from datetime import date
from datetime import datetime

from sqlalchemy import Boolean
from sqlalchemy import Date
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.dialects.postgresql import UUID as PG_UUID

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.core.base import Base


class StudyTopic(Base):

    __tablename__ = "study_topics"

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

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    subject: Mapped[str | None] = mapped_column(
        String(120),
        nullable=True,
        index=True,
    )

    target_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
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
