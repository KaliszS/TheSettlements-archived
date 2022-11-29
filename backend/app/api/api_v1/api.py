from fastapi import APIRouter

from app.api.api_v1.endpoints import settlement

api_router = APIRouter()

api_router.include_router(settlement.router, prefix="/settlement", tags=["settlements"])