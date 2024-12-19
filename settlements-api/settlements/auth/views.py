from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from settlements.database import DbSession
from settlements.auth.services import auth_services
from settlements.users.services import user_services


router = APIRouter()

@router.get("/login", status_code=status.HTTP_200_OK)
async def login(db: DbSession, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    if not (user := user_services.get_by_name(db, form_data.username)):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect username")

    if not user.password == form_data.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect password")

    return {"access_token": user.name, "token_type": "bearer"}