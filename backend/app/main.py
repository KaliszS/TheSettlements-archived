from fastapi import FastAPI, APIRouter

from app.core.config import settings
from app.db.session import db
from app.api.api_v1.api import api_router, auth_router

app = FastAPI(
    title="The Settlements API"
)

@app.on_event("startup")
def startup_event():
    db.connect(settings.MONGODB_DATABASE_URI, settings.PORT)
    db.get_database(settings.MONGO_DATABASE_NAME)

@app.on_event("shutdown")
def shutdown_event():
    db.close()

root_router = APIRouter()

app.include_router(auth_router, prefix=settings.API_V_LATEST_STR)
app.include_router(api_router, prefix=settings.API_V_LATEST_STR)
app.include_router(root_router)

if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8010, log_level="debug")