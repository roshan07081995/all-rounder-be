from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import StudyTopic


class StudyTopicRepository:

    def __init__(
        self,
        db: AsyncSession,
    ):
        self.db = db

    async def create(
        self,
        topic: StudyTopic,
    ):

        self.db.add(topic)

        await self.db.commit()

        await self.db.refresh(topic)

        return topic

    async def get_by_id(
        self,
        topic_id: UUID,
    ):

        stmt = (
            select(StudyTopic)
            .where(StudyTopic.id == topic_id)
        )

        result = await self.db.execute(stmt)

        return result.scalar_one_or_none()

    async def get_all_by_user(
        self,
        user_id: int,
    ):

        stmt = (
            select(StudyTopic)
            .where(StudyTopic.user_id == user_id)
            .order_by(StudyTopic.created_at.desc())
        )

        result = await self.db.execute(stmt)

        return result.scalars().all()

    async def update(
        self,
        topic: StudyTopic,
    ):

        await self.db.commit()
        await self.db.refresh(topic)
        return topic

    async def delete(
        self,
        topic: StudyTopic,
    ):

        await self.db.delete(topic)

        await self.db.commit()
