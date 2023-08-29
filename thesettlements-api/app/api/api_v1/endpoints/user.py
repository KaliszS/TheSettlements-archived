from fastapi import APIRouter, Query, Depends

from app.api import crud, dependencies as deps
from app import schemas

router = APIRouter()
collection = deps.get_collection(__file__)


# <----------------- POST ----------------->


# <----------------- GET ----------------->
@router.get("/", response_model=list[schemas.User])
async def read_all_users(skip: int = Query(0, ge=0), limit: int = Query(100, ge=0)):
    return await crud.read_all(collection, skip, limit)

@router.get("/{id}", response_model=schemas.User)
async def read_user_by_id(id: str):
    return await crud.read_by_id(id, collection)

# <----------------- PUT ----------------->
@router.put("/{id}", response_model=schemas.User)
async def update_user(id: str, model_in: schemas.UserUpdate):
    return await crud.update(id, model_in, collection)

# <----------------- DELETE ----------------->
@router.delete("/")
async def delete_all_users():
    return await crud.delete_all(collection)

@router.delete("/{id}")
async def delete_user(id: str):
    return await crud.delete(id, collection)