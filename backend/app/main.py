import time

from fastapi import FastAPI, APIRouter, Request

from app.core.config import settings
from app.api.api_v1.api import api_router

app = FastAPI(
    title="The Settlements API"
)

root_router = APIRouter()

app.include_router(api_router, prefix=settings.API_V_LATEST_STR)
app.include_router(root_router)

if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8010, log_level="debug")