from fastapi import APIRouter, Depends

from app.api import dependencies as deps
from app.api.api_v1.endpoints import auth, settlement

api_router = APIRouter(dependencies=[Depends(deps.get_current_user)])

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(settlement.router, prefix="/settlement", tags=["settlements"])