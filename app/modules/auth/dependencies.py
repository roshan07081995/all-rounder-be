from fastapi import Depends

from app.core.database import get_db
from fastapi import HTTPException
from fastapi.security import HTTPAuthorizationCredentials
from app.modules.auth.repository import (
    AuthRepository,
)
from fastapi.security import HTTPBearer
from app.modules.auth.service import (
    AuthService,
)
from app.core.config import settings
from jose import JWTError, jwt

security = HTTPBearer()

def get_auth_service(
    db=Depends(get_db),
) -> AuthService:

    repository = AuthRepository(db)

    return AuthService(repository)

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(
        security
    ),
):

    token = credentials.credentials

    try:

        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
        )
        print(payload)
        return {
            "id": int(payload["sub"])
        }

    except JWTError as e:
        print("JWT ERROR:", repr(e))
        raise HTTPException(
            status_code=401,
            detail=str(e),
        )