from uuid import UUID

from fastapi import APIRouter
from fastapi import Depends

from app.modules.auth.dependencies import (
    get_current_user,
)

from .dependencies import (
    get_daily_task_service,
)

from .schemas import (
    CreateTaskRequest,
    UpdateTaskRequest,
    TaskResponse
)

from .schemas import TaskResponse
from .service import DailyTaskService

router = APIRouter(
    prefix="/tasks",
    tags=["Daily Tasks"],
)

@router.post(
    "",
    response_model=TaskResponse,
)
async def create_task(

    payload: CreateTaskRequest,

    current_user=Depends(
        get_current_user
    ),

    service=Depends(
        get_daily_task_service
    ),
):

    return await service.create_task(

        current_user["id"],

        payload,

    )

@router.get(
    "",
    response_model=list[TaskResponse],
)
async def get_tasks(

    current_user=Depends(
        get_current_user
    ),

    service=Depends(
        get_daily_task_service
    ),
):

    return await service.get_tasks(

        current_user["id"]

    )

@router.get(
    "/{task_id}",
    response_model=TaskResponse,
)
async def get_task(

    task_id: UUID,

    current_user=Depends(
        get_current_user
    ),

    service=Depends(
        get_daily_task_service
    ),
):

    return await service.get_task(

        current_user["id"],

        task_id,

    )

@router.put(
    "/{task_id}",
    response_model=TaskResponse,
)
async def update_task(
    task_id: UUID,
    payload: UpdateTaskRequest,
    current_user=Depends(get_current_user),
    service: DailyTaskService = Depends(
        get_daily_task_service
    ),
):

    return await service.update_task(
        task_id=task_id,
        user_id=current_user["id"],
        payload=payload,
    )

@router.delete("/{task_id}")
async def delete_task(
    task_id: UUID,
    current_user=Depends(get_current_user),
    service: DailyTaskService = Depends(
        get_daily_task_service
    ),
):

    return await service.delete_task(
        task_id=task_id,
        user_id=current_user["id"],
    )