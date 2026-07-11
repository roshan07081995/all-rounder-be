from uuid import UUID

from fastapi import APIRouter
from fastapi import Depends

from app.modules.auth.dependencies import (
    get_current_user,
)

from .dependencies import (
    get_study_topic_service,
)
from .schemas import (
    CreateStudyTopicRequest,
    StudyTopicResponse,
    UpdateStudyTopicRequest,
)
from .service import StudyTopicService


router = APIRouter(
    prefix="/study-topics",
    tags=["Study Topics"],
)


@router.post(
    "",
    response_model=StudyTopicResponse,
)
async def create_study_topic(
    payload: CreateStudyTopicRequest,
    current_user=Depends(get_current_user),
    service: StudyTopicService = Depends(
        get_study_topic_service
    ),
):

    return await service.create_topic(
        user_id=current_user["id"],
        payload=payload,
    )


@router.get(
    "",
    response_model=list[StudyTopicResponse],
)
async def get_study_topics(
    current_user=Depends(get_current_user),
    service: StudyTopicService = Depends(
        get_study_topic_service
    ),
):

    return await service.get_topics(
        user_id=current_user["id"],
    )


@router.get(
    "/{topic_id}",
    response_model=StudyTopicResponse,
)
async def get_study_topic(
    topic_id: UUID,
    current_user=Depends(get_current_user),
    service: StudyTopicService = Depends(
        get_study_topic_service
    ),
):

    return await service.get_topic(
        user_id=current_user["id"],
        topic_id=topic_id,
    )


@router.put(
    "/{topic_id}",
    response_model=StudyTopicResponse,
)
async def update_study_topic(
    topic_id: UUID,
    payload: UpdateStudyTopicRequest,
    current_user=Depends(get_current_user),
    service: StudyTopicService = Depends(
        get_study_topic_service
    ),
):

    return await service.update_topic(
        topic_id=topic_id,
        user_id=current_user["id"],
        payload=payload,
    )


@router.delete(
    "/{topic_id}",
)
async def delete_study_topic(
    topic_id: UUID,
    current_user=Depends(get_current_user),
    service: StudyTopicService = Depends(
        get_study_topic_service
    ),
):

    return await service.delete_topic(
        topic_id=topic_id,
        user_id=current_user["id"],
    )
