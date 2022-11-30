import os

from dotenv import load_dotenv, find_dotenv
from pydantic import BaseSettings, AnyHttpUrl, validator

class Settings(BaseSettings):
    env_loc = find_dotenv(".env")
    load_dotenv(env_loc)

    API_V1_STR: str = "/api/v1"
    API_V_LATEST_STR: str = API_V1_STR

    JWT_SECRET: str = os.environ.get("JWT_SECRET")
    ALGORITHM: str = os.environ.get("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60*24

    # e.g: ["http://localhost", "http://localhost:8080"]
    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: str | list[str]) -> list[str] | str:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    class Config:
        case_sensitive = True

    MONGODB_DATABASE_URI: str | None = "db"
    PORT: int | None = int(os.environ.get("MONGO_PORT"))
    DATABASE_NAME: str | None = os.environ.get("DATABASE_NAME")

settings = Settings()
