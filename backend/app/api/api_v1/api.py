from fastapi import APIRouter, Depends

from app.api import dependencies as deps
from app.api.api_v1 import auth
from app.api.api_v1.endpoints import settlement

auth_router = APIRouter()
api_router = APIRouter(dependencies=[Depends(deps.get_current_user)])

auth_router.include_router(auth.router, prefix="/auth", tags=["auth"])

api_router.include_router(settlement.router, prefix="/settlement", tags=["settlements"])