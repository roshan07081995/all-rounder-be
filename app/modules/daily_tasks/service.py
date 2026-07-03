from uuid import UUID

from fastapi import HTTPException

from .models import DailyTask

from .repository import DailyTaskRepository

from .schemas import CreateTaskRequest

from .schemas import UpdateTaskRequest


class DailyTaskService:

    def __init__(
        self,
        repository: DailyTaskRepository,
    ):

        self.repository = repository

    async def create_task(

        self,

        user_id: int,

        payload: CreateTaskRequest,

    ):

        task = DailyTask(

            user_id=user_id,

            title=payload.title,

            description=payload.description,

            priority=payload.priority,

            due_date=payload.due_date,

        )

        return await self.repository.create(task)

    async def get_tasks(

        self,

        user_id: UUID,

    ):

        return await self.repository.get_all_by_user(
            user_id
        )

    async def get_task(

        self,

        user_id: UUID,

        task_id: UUID,

    ):

        task = await self.repository.get_by_id(
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
                detail="Forbidden",
            )

        return task
    
    async def update_task(
        self,
        task_id: UUID,
        user_id: int,
        payload: UpdateTaskRequest,
    ):

        task = await self.repository.get_by_id(task_id)

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

        update_data = payload.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(task, key, value)

        return await self.repository.update(task)

    async def delete_task(
        self,
        task_id: UUID,
        user_id: int,
    ):

        task = await self.repository.get_by_id(task_id)

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

        await self.repository.delete(task)

        return {
            "message": "Task deleted successfully"
        }