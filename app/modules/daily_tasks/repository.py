from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import DailyTask


class DailyTaskRepository:

    def __init__(
        self,
        db: AsyncSession,
    ):
        self.db = db

    async def create(
        self,
        task: DailyTask,
    ):

        self.db.add(task)

        await self.db.commit()

        await self.db.refresh(task)

        return task

    async def get_by_id(
        self,
        task_id: UUID,
    ):

        stmt = (
            select(DailyTask)
            .where(DailyTask.id == task_id)
        )

        result = await self.db.execute(stmt)

        return result.scalar_one_or_none()

    async def get_all_by_user(
        self,
        user_id: UUID,
    ):

        stmt = (
            select(DailyTask)
            .where(DailyTask.user_id == user_id)
            .order_by(DailyTask.created_at.desc())
        )

        result = await self.db.execute(stmt)

        return result.scalars().all()

    async def update(self, task):

        await self.db.commit()
        await self.db.refresh(task)
        return task

    async def delete(
        self,
        task: DailyTask,
    ):

        await self.db.delete(task)

        await self.db.commit()