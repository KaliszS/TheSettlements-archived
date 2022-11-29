from fastapi import APIRouter, Query

from app.api import deps, crud
from app import schemas

router = APIRouter()
collection = deps.getCollection(__file__)

# current_user: deps.CurrentUser = deps.get_current_active_user(),

# <----------------- POST ----------------->
@router.post("/", response_model=schemas.Settlement)
async def create_settlement(model_in: schemas.Settlement):
    model_out = await crud.create(model_in, collection)
    return model_out

# <----------------- GET ----------------->
@router.get("/", response_model=list[schemas.Settlement])
async def read_all_settlements(skip: int = Query(0, ge=0), limit: int = Query(100, ge=0)):
    results = await crud.read_all(collection, skip, limit)
    return results

@router.get("/{id}", response_model=schemas.Settlement)
async def read_settlement_by_id(id: str):
    model_out = await crud.read_by_id(id, collection)
    return model_out

# <----------------- PUT ----------------->
@router.put("/{id}", response_model=schemas.Settlement)
async def update_settlement(id: str, model_in: schemas.SettlementUpdate):
    model_out = await crud.update(id, model_in, collection)
    return model_out

# <----------------- DELETE ----------------->
@router.delete("/")
async def delete_all_settlements():
    result = await crud.delete_all(collection)
    return result

@router.delete("/{id}")
async def delete_settlement(id: str):
    result = await crud.delete(id, collection)
    return result