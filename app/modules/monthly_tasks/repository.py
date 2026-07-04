from uuid import UUID

from datetime import date

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.daily_tasks.models import DailyTask

from .models import MonthlyTaskCompletion


class MonthlyTaskRepository:

    def __init__(
        self,
        db: AsyncSession,
    ):
        self.db = db

    async def get_task_by_id(
        self,
        task_id: UUID,
    ):

        stmt = (
            select(DailyTask)
            .where(DailyTask.id == task_id)
        )

        result = await self.db.execute(stmt)

        return result.scalar_one_or_none()

    async def get_by_task_and_date(
        self,
        user_id: int,
        task_id: UUID,
        completion_date: date,
    ):

        stmt = (
            select(MonthlyTaskCompletion)
            .where(MonthlyTaskCompletion.user_id == user_id)
            .where(MonthlyTaskCompletion.task_id == task_id)
            .where(
                MonthlyTaskCompletion.completion_date
                == completion_date
            )
        )

        result = await self.db.execute(stmt)

        return result.scalar_one_or_none()

    async def get_by_id(
        self,
        completion_id: UUID,
    ):

        stmt = (
            select(MonthlyTaskCompletion)
            .where(MonthlyTaskCompletion.id == completion_id)
        )

        result = await self.db.execute(stmt)

        return result.scalar_one_or_none()

    async def get_by_month(
        self,
        user_id: int,
        start_date: date,
        end_date: date,
    ):

        stmt = (
            select(MonthlyTaskCompletion)
            .where(MonthlyTaskCompletion.user_id == user_id)
            .where(
                MonthlyTaskCompletion.completion_date >= start_date
            )
            .where(
                MonthlyTaskCompletion.completion_date <= end_date
            )
            .order_by(
                MonthlyTaskCompletion.completion_date.asc(),
                MonthlyTaskCompletion.created_at.desc(),
            )
        )

        result = await self.db.execute(stmt)

        return result.scalars().all()

    async def create(
        self,
        completion: MonthlyTaskCompletion,
    ):

        self.db.add(completion)

        await self.db.commit()

        await self.db.refresh(completion)

        return completion

    async def update(
        self,
        completion: MonthlyTaskCompletion,
    ):

        await self.db.commit()

        await self.db.refresh(completion)

        return completion

    async def delete(
        self,
        completion: MonthlyTaskCompletion,
    ):

        await self.db.delete(completion)

        await self.db.commit()
