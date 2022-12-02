from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient

from app.core.auth import oauth2_scheme
from app.core.config import settings
from app.db.session import db
from app.schemas.user import User
from app.utils import filename

class TokenData(BaseModel):
    username: str | None = None

def get_collection(fileObject):
    collection_name = filename.get_filename(fileObject)
    return db.client.database[collection_name]

def get_db():
    return db.client.database

async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.ALGORITHM], options={"verify_aud": False})
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception

    user = await db["user"].find_one({"username": token_data.username})
    if user is None:
        raise credentials_exception
    
    return user