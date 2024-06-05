from functools import lru_cache

from pydantic import SecretStr, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file_encoding="utf-8", extra="ignore")

    # General
    environment: str = "dev"
    release: str = "dev"
    debug: bool = False

    # Database
    pg_host: str = "localhost"
    pg_port: int = 5432
    pg_database: str = "postgres"
    pg_user: str = "user"
    pg_password: SecretStr = SecretStr("password")

    @property
    def database_uri(self) -> PostgresDsn:
        return (
            f"postgresql+psycopg://"
            f"{self.pg_user}:{self.pg_password.get_secret_value()}"
            f"@{self.pg_host}:{self.pg_port}/{self.pg_database}"
        )

    # Token
    # jwt_secret: str
    jwt_algorithm: str = "HS256"
    jwt_access_token_expire_minutes: int = 60 * 24


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
