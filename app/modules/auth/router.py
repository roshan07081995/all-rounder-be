from fastapi import APIRouter
from fastapi import Depends

from app.modules.auth.schemas import (
    RegisterRequest,
    LoginRequest,
)

from app.modules.auth.dependencies import (
    get_auth_service,
)

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/register")
async def register(
    payload: RegisterRequest,
    service=Depends(
        get_auth_service
    ),
):
    return await service.register(
        payload.email,
        payload.password,
    )


@router.post("/login")
async def login(
    payload: LoginRequest,
    service=Depends(
        get_auth_service
    ),
):
    return await service.login(
        payload.email,
        payload.password,
    )