import time
from uuid import UUID

import jwt

from settlements.config import settings


class AccessToken:
    def __init__(self):
        self.token = None
        self.secret = settings.jwt_secret
        self.algorithm = settings.jwt_algorithm

    @property
    def response(self) -> dict[str, str]:
        return {"access_token": self.token}

    def sign_jwt(self, user_id: UUID) -> None:
        payload = {
            "user_id": str(user_id),
            "exp": time.time() + settings.jwt_access_token_expire_seconds,
        }
        self.token = jwt.encode(payload, self.secret, algorithm=self.algorithm)

    def decode_jwt(self) -> dict[str, str] | None:
        try:
            decoded_token = jwt.decode(self.token, self.secret, algorithms=[self.algorithm])
            return decoded_token if decoded_token["exp"] >= time.time() else None
        except jwt.InvalidTokenError:
            return


# from typing import MutableMapping
# from datetime import datetime, timedelta

# from fastapi.security import OAuth2PasswordBearer
# import jwt

# from app.config import settings
# from app.utils.security import verify_password
# from app.users.schemas import UserRead


# JWTPayloadMapping = MutableMapping[str, datetime | bool | str | list[str] | list[int]]

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V_LATEST_STR}/auth/login")


# async def authenticate(username: str, password: str, collection) -> UserRead | None:
#     user = await collection.find_one({"username": username})
#     if not user:
#         return None
#     if not verify_password(password, user["hashed_password"]):
#         return None
#     return user


# def create_access_token(sub: str) -> str:
#     return _create_token(
#         token_type="access_token",
#         lifetime=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
#         sub=sub,
#     )


# def _create_token(token_type: str, lifetime: timedelta, sub: str) -> str:
#     payload = {}
#     expire = datetime.utcnow() + lifetime
#     payload["type"] = token_type
#     payload["exp"] = expire
#     payload["iat"] = datetime.utcnow()
#     payload["sub"] = str(sub)

#     return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.ALGORITHM)
