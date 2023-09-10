from functools import lru_cache

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    # General
    environment: str = "dev"
    release: str = "dev"
    debug: bool = False

    # Database
    neo4j_host: str = "localhost"
    neo4j_port: str = "7687"
    neo4j_username: str = "neo4j"
    neo4j_password: SecretStr = SecretStr("password")
    neo4j_db_name: str = "TheSettlements"

    @property
    def database_uri(self) -> str:
        return f"bolt://" f"{self.neo4j_host}:" f"{self.neo4j_port}"

    # Token
    jwt_secret: str
    jwt_algorithm: str = "HS256"
    jwt_access_token_expire_minutes: int = 60 * 24


@lru_cache()
def get_settings() -> BaseSettings:
    return Settings()


settings = get_settings()
