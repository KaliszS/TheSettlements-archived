from fastapi import FastAPI

from settlements.config import settings
from settlements.api import api_router


api = FastAPI(
    title="The Settlements API",
)


@api.get("/")
async def root():
    return {"message": "Game engine is running!"}


api.include_router(api_router, prefix=settings.api_latest, tags=["API v1"])
