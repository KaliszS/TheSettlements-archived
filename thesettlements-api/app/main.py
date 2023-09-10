from fastapi import FastAPI, APIRouter, Depends
from neo4j import Driver

from app.config import settings
from app.database import get_driver

# from app.api.api_v1.api import api_router, auth_router


app = FastAPI(
    title="The Settlements API",
)

root_router = APIRouter()


@root_router.get("/")
async def get_all_objects_from_neo4j(driver: Driver = Depends(get_driver)):
    with driver.session() as session:
        result = session.run("MATCH (n) RETURN n")
        return result.data()


# app.include_router(auth_router, prefix=settings.API_V_LATEST_STR)
# app.include_router(api_router, prefix=settings.API_V_LATEST_STR)
app.include_router(root_router)
