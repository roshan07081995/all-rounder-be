from uuid import UUID

from calendar import monthrange
from datetime import date

from fastapi import HTTPException

from .models import MonthlyTaskCompletion
from .repository import MonthlyTaskRepository
from .schemas import MonthlyTaskCompletionBulkRequest
from .schemas import MonthlyTaskCompletionRequest


class MonthlyTaskService:

    def __init__(
        self,
        repository: MonthlyTaskRepository,
    ):

        self.repository = repository

    async def save_completion(
        self,
        user_id: int,
        payload: MonthlyTaskCompletionRequest,
    ):

        await self._validate_task_owner(
            user_id=user_id,
            task_id=payload.task_id,
        )

        completion = await self.repository.get_by_task_and_date(
            user_id=user_id,
            task_id=payload.task_id,
            completion_date=payload.completion_date,
        )

        if completion:
            completion.is_completed = payload.is_completed

            return await self.repository.update(completion)

        completion = MonthlyTaskCompletion(
            user_id=user_id,
            task_id=payload.task_id,
            completion_date=payload.completion_date,
            is_completed=payload.is_completed,
        )

        return await self.repository.create(completion)

    async def save_completions(
        self,
        user_id: int,
        payload: MonthlyTaskCompletionBulkRequest,
    ):

        completions = []

        for item in payload.items:
            completion = await self.save_completion(
                user_id=user_id,
                payload=item,
            )

            completions.append(completion)

        return completions

    async def get_monthly_completions(
        self,
        user_id: int,
        year: int,
        month: int,
    ):

        if month < 1 or month > 12:
            raise HTTPException(
                status_code=400,
                detail="Month must be between 1 and 12",
            )

        start_date = date(year, month, 1)
        end_date = date(
            year,
            month,
            monthrange(year, month)[1],
        )

        return await self.repository.get_by_month(
            user_id=user_id,
            start_date=start_date,
            end_date=end_date,
        )

    async def delete_completion(
        self,
        user_id: int,
        completion_id: UUID,
    ):

        completion = await self.repository.get_by_id(
            completion_id
        )

        if completion is None:
            raise HTTPException(
                status_code=404,
                detail="Monthly task completion not found",
            )

        if completion.user_id != user_id:
            raise HTTPException(
                status_code=403,
                detail="Access denied",
            )

        await self.repository.delete(completion)

        return {
            "message": "Monthly task completion deleted successfully"
        }

    async def _validate_task_owner(
        self,
        user_id: int,
        task_id: UUID,
    ):

        task = await self.repository.get_task_by_id(
            task_id
        )

        if task is None:
            raise HTTPException(
                status_code=404,
                detail="Task not found",
            )

        if task.user_id != user_id:
            raise HTTPException(
                status_code=403,
                detail="Access denied",
            )
