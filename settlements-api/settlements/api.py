from fastapi import APIRouter

from settlements.cities.views import router as cities_router


api_router = APIRouter()


api_router.include_router(cities_router, prefix="/cities", tags=["cities"])
