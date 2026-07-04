from uuid import UUID

from datetime import date
from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict


class MonthlyTaskCompletionRequest(BaseModel):

    task_id: UUID

    completion_date: date

    is_completed: bool


class MonthlyTaskCompletionBulkRequest(BaseModel):

    items: list[MonthlyTaskCompletionRequest]


class MonthlyTaskCompletionResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: UUID

    user_id: int

    task_id: UUID

    completion_date: date

    is_completed: bool

    created_at: datetime

    updated_at: datetime


class MonthlyTaskCompletionBulkResponse(BaseModel):

    items: list[MonthlyTaskCompletionResponse]
