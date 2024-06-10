from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from pydantic import BaseModel

from app.utils.auth import oauth2_scheme
from app.config import settings
from app.database import db
from app.users.schemas import UserBase
from app.utils import filename


class TokenData(BaseModel):
    username: str | None = None


def get_collection(fileObject):
    collection_name = filename.get_filename(fileObject)
    return get_db()[collection_name]


def get_db():
    return db.client.database


async def get_current_user(token: str = Depends(oauth2_scheme)) -> UserBase:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=[settings.ALGORITHM],
            options={"verify_aud": False},
        )
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception

    user = await get_db()["user"].find_one({"username": token_data.username})
    if user is None:
        raise credentials_exception

    return user
