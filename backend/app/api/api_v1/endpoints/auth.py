from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.core.security import get_password_hash
from app.core.auth import authenticate, create_access_token
from app.db.session import db
from app.api import deps, crud
from app import schemas

router = APIRouter()
collection = db["user"]

@router.post("/signup", response_model=schemas.User)
async def create_user(user_in: schemas.UserCreate):
    if (user := await collection.find_one({"email": user_in.email})) is not None:
        raise HTTPException(status_code=400, detail=f"Email {user_in.email} already registered")

    if (user := await collection.find_one({"username": user_in.username})) is not None:
        raise HTTPException(status_code=400, detail=f"Username {user_in.username} already taken")

    user_dict = jsonable_encoder(user_in)
    user_dict.pop("password")
    user_db = schemas.UserInDB(**user_dict, hashed_password = get_password_hash(user_in.password))
    user_created = await collection.insert_one(jsonable_encoder(user_db))
    user_out = await collection.find_one({"_id": user_created.inserted_id})

    return JSONResponse(status_code=status.HTTP_201_CREATED, content=user_out)

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate(username=form_data.username, password=form_data.password, collection=collection)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {
        "access_token": create_access_token(sub=user["_id"]),
        "token_type": "bearer",
    }

@router.get("/me", response_model=schemas.User)
async def read_users_me():  
    current_user = deps.get_current_user(collection=collection)
    return current_user

@router.get("/users", response_model=list[schemas.User])
async def read_all_users():
    users = await crud.read_all(collection=collection)
    return users

@router.delete("/users")
async def delete_all_users():
    delete_result = await crud.delete_all(collection=collection)
    return delete_result