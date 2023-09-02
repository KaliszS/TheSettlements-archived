from contextlib import asynccontextmanager

from fastapi import FastAPI, APIRouter, Depends
from neo4j import AsyncDriver

from app.config import settings
from app.database import get_driver
from app.api.api_v1.api import api_router, auth_router

@asynccontextmanager
async def verify_connection(driver: AsyncDriver = Depends(get_driver)) -> None:
    async with driver:
        driver.verify_connectivity()

app = FastAPI(
    title="The Settlements API"
    lifespan=verify_connection,
)

root_router = APIRouter()

app.include_router(auth_router, prefix=settings.API_V_LATEST_STR)
app.include_router(api_router, prefix=settings.API_V_LATEST_STR)
app.include_router(root_router)