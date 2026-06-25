from fastapi import HTTPException
from fastapi import status

from app.modules.auth.repository import (
    AuthRepository,
)

from app.modules.auth.security import (
    hash_password,
    verify_password,
    create_access_token,
)


class AuthService:

    def __init__(
        self,
        repository: AuthRepository,
    ):
        self.repository = repository

    async def register(
        self,
        email: str,
        password: str,
    ):

        existing_user = (
            await self.repository.get_by_email(
                email
            )
        )

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User already exists",
            )

        user = (
            await self.repository.create_user(
                email=email,
                hashed_password=hash_password(
                    password
                ),
            )
        )

        token = create_access_token(
            user.id
        )

        return {
            "access_token": token,
            "token_type": "bearer",
        }

    async def login(
        self,
        email: str,
        password: str,
    ):

        user = (
            await self.repository.get_by_email(
                email
            )
        )

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials",
            )

        if not verify_password(
            password,
            user.hashed_password,
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials",
            )

        token = create_access_token(
            user.id
        )

        return {
            "access_token": token,
            "token_type": "bearer",
        }