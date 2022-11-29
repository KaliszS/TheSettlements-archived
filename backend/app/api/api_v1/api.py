from fastapi import APIRouter

from app.api.api_v1.endpoints import auth, settlement

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(settlement.router, prefix="/settlement", tags=["settlements"])