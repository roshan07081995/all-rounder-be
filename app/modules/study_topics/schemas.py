from uuid import UUID
from datetime import date
from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict


class CreateStudyTopicRequest(BaseModel):

    title: str

    description: str | None = None

    subject: str | None = None

    target_date: date | None = None

    is_completed: bool = False


class UpdateStudyTopicRequest(BaseModel):

    title: str | None = None

    description: str | None = None

    subject: str | None = None

    target_date: date | None = None

    is_completed: bool | None = None


class StudyTopicResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: UUID

    title: str

    description: str | None

    subject: str | None

    target_date: date | None

    is_completed: bool

    created_at: datetime

    updated_at: datetime
