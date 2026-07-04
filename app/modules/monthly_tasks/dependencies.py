from fastapi import Depends

from app.core.database import get_db

from .repository import MonthlyTaskRepository
from .service import MonthlyTaskService


def get_monthly_task_service(
    db=Depends(get_db),
):

    repository = MonthlyTaskRepository(db)

    return MonthlyTaskService(repository)
