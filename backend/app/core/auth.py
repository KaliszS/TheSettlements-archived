from typing import MutableMapping
from datetime import datetime, timedelta

from fastapi.security import OAuth2PasswordBearer
from jose import jwt

from app.core.config import settings
from app.core.security import verify_password
from app.schemas.user import User, UserInDB


JWTPayloadMapping = MutableMapping[str, datetime | bool | str | list[str] | list[int]]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V_LATEST_STR}/auth/login")


async def authenticate(username: str, password: str, collection) -> User | None:
    user = await collection.find_one({"username": username})
    if not user:
        return None
    if not verify_password(password, user["hashed_password"]):
        return None
    return user

def create_access_token(sub: str) -> str:
    return _create_token(
        token_type="access_token",
        lifetime=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        sub=sub,
    )

def _create_token(token_type: str, lifetime: timedelta, sub: str) -> str:
    payload = {}
    expire = datetime.utcnow() + lifetime
    payload["type"] = token_type
    payload["exp"] = expire
    payload["iat"] = datetime.utcnow()
    payload["sub"] = str(sub)

    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.ALGORITHM)