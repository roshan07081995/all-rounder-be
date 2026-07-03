from uuid import UUID
from datetime import date
from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict

from .constants import TaskPriority
from .constants import TaskStatus


class CreateTaskRequest(BaseModel):

    title: str

    description: str | None = None

    priority: TaskPriority = TaskPriority.MEDIUM

    due_date: date | None = None


class UpdateTaskRequest(BaseModel):

    title: str | None = None

    description: str | None = None

    priority: TaskPriority | None = None

    due_date: date | None = None

    status: TaskStatus | None = None


class TaskResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: UUID

    title: str

    description: str | None

    priority: TaskPriority

    status: TaskStatus

    due_date: date | None

    created_at: datetime

    updated_at: datetime