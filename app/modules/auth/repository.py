from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.auth.models import User


class AuthRepository:

    def __init__(
        self,
        db: AsyncSession,
    ):
        self.db = db

    async def get_by_email(
        self,
        email: str,
    ):

        stmt = select(User).where(
            User.email == email
        )

        result = await self.db.execute(stmt)

        return result.scalar_one_or_none()

    async def create_user(
        self,
        email: str,
        hashed_password: str,
    ):

        user = User(
            email=email,
            hashed_password=hashed_password,
        )

        self.db.add(user)

        await self.db.commit()

        await self.db.refresh(user)

        return user