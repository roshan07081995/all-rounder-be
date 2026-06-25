from fastapi import Depends

from app.core.database import get_db

from app.modules.auth.repository import (
    AuthRepository,
)

from app.modules.auth.service import (
    AuthService,
)


def get_auth_service(
    db=Depends(get_db),
) -> AuthService:

    repository = AuthRepository(db)

    return AuthService(repository)