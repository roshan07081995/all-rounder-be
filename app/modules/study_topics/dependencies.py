from fastapi import Depends

from app.core.database import get_db

from .repository import StudyTopicRepository
from .service import StudyTopicService


def get_study_topic_service(
    db=Depends(get_db),
):

    repository = StudyTopicRepository(db)

    return StudyTopicService(repository)
