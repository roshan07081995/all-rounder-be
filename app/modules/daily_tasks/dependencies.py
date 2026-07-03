from fastapi import Depends

from app.core.database import get_db

from .repository import DailyTaskRepository

from .service import DailyTaskService
from jose import jwt

def get_daily_task_service(
    db=Depends(get_db),
):

    repository = DailyTaskRepository(db)

    return DailyTaskService(repository)