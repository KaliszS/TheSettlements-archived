from fastapi import APIRouter, Query

from app.api import crud, dependencies as deps
from app import schemas

router = APIRouter()
collection = deps.get_collection(__file__)


# <----------------- POST ----------------->
@router.post("/", response_model=schemas.Settlement)
async def create_settlement(model_in: schemas.Settlement):
    return await crud.create(model_in, collection)


# <----------------- GET ----------------->
@router.get("/", response_model=list[schemas.Settlement])
async def read_all_settlements(
    skip: int = Query(0, ge=0), limit: int = Query(100, ge=0)
):
    return await crud.read_all(collection, skip, limit)


@router.get("/{id}", response_model=schemas.Settlement)
async def read_settlement_by_id(id: str):
    return await crud.read_by_id(id, collection)


# <----------------- PUT ----------------->
@router.put("/{id}", response_model=schemas.Settlement)
async def update_settlement(id: str, model_in: schemas.SettlementUpdate):
    return await crud.update(id, model_in, collection)


# <----------------- DELETE ----------------->
@router.delete("/")
async def delete_all_settlements():
    return await crud.delete_all(collection)


@router.delete("/{id}")
async def delete_settlement(id: str):
    return await crud.delete(id, collection)
