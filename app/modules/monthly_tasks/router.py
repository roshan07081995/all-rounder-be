from uuid import UUID

from fastapi import APIRouter
from fastapi import Depends

from app.modules.auth.dependencies import (
    get_current_user,
)

from .dependencies import (
    get_monthly_task_service,
)
from .schemas import (
    MonthlyTaskCompletionBulkRequest,
    MonthlyTaskCompletionBulkResponse,
    MonthlyTaskCompletionRequest,
    MonthlyTaskCompletionResponse,
)
from .service import MonthlyTaskService


router = APIRouter(
    prefix="/monthly-tasks",
    tags=["Monthly Tasks"],
)


@router.post(
    "",
    response_model=MonthlyTaskCompletionResponse,
)
async def save_completion(
    payload: MonthlyTaskCompletionRequest,
    current_user=Depends(get_current_user),
    service: MonthlyTaskService = Depends(
        get_monthly_task_service
    ),
):

    return await service.save_completion(
        user_id=current_user["id"],
        payload=payload,
    )


@router.post(
    "/bulk",
    response_model=MonthlyTaskCompletionBulkResponse,
)
async def save_completions(
    payload: MonthlyTaskCompletionBulkRequest,
    current_user=Depends(get_current_user),
    service: MonthlyTaskService = Depends(
        get_monthly_task_service
    ),
):

    completions = await service.save_completions(
        user_id=current_user["id"],
        payload=payload,
    )

    return {
        "items": completions
    }


@router.get(
    "",
    response_model=list[MonthlyTaskCompletionResponse],
)
async def get_monthly_completions(
    year: int,
    month: int,
    current_user=Depends(get_current_user),
    service: MonthlyTaskService = Depends(
        get_monthly_task_service
    ),
):

    return await service.get_monthly_completions(
        user_id=current_user["id"],
        year=year,
        month=month,
    )


@router.delete(
    "/{completion_id}",
)
async def delete_completion(
    completion_id: UUID,
    current_user=Depends(get_current_user),
    service: MonthlyTaskService = Depends(
        get_monthly_task_service
    ),
):

    return await service.delete_completion(
        user_id=current_user["id"],
        completion_id=completion_id,
    )
