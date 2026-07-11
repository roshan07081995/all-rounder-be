from uuid import UUID

from fastapi import HTTPException

from .models import StudyTopic
from .repository import StudyTopicRepository
from .schemas import CreateStudyTopicRequest
from .schemas import UpdateStudyTopicRequest


class StudyTopicService:

    def __init__(
        self,
        repository: StudyTopicRepository,
    ):

        self.repository = repository

    async def create_topic(
        self,
        user_id: int,
        payload: CreateStudyTopicRequest,
    ):

        topic = StudyTopic(
            user_id=user_id,
            title=payload.title,
            description=payload.description,
            subject=payload.subject,
            target_date=payload.target_date,
            is_completed=payload.is_completed,
        )

        return await self.repository.create(topic)

    async def get_topics(
        self,
        user_id: int,
    ):

        return await self.repository.get_all_by_user(
            user_id
        )

    async def get_topic(
        self,
        user_id: int,
        topic_id: UUID,
    ):

        topic = await self.repository.get_by_id(
            topic_id
        )

        if topic is None:
            raise HTTPException(
                status_code=404,
                detail="Study topic not found",
            )

        if topic.user_id != user_id:
            raise HTTPException(
                status_code=403,
                detail="Access denied",
            )

        return topic

    async def update_topic(
        self,
        topic_id: UUID,
        user_id: int,
        payload: UpdateStudyTopicRequest,
    ):

        topic = await self.repository.get_by_id(
            topic_id
        )

        if topic is None:
            raise HTTPException(
                status_code=404,
                detail="Study topic not found",
            )

        if topic.user_id != user_id:
            raise HTTPException(
                status_code=403,
                detail="Access denied",
            )

        update_data = payload.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(topic, key, value)

        return await self.repository.update(topic)

    async def delete_topic(
        self,
        topic_id: UUID,
        user_id: int,
    ):

        topic = await self.repository.get_by_id(
            topic_id
        )

        if topic is None:
            raise HTTPException(
                status_code=404,
                detail="Study topic not found",
            )

        if topic.user_id != user_id:
            raise HTTPException(
                status_code=403,
                detail="Access denied",
            )

        await self.repository.delete(topic)

        return {
            "message": "Study topic deleted successfully"
        }
