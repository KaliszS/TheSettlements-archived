from collections.abc import AsyncGenerator
from typing import Annotated, Iterator

from fastapi import Depends
from neo4j import AsyncGraphDatabase, AsyncDriver, Session

from .config import settings

async def get_driver() -> Iterator[AsyncDriver]:
    URI: str = settings.database_uri
    AUTH: tuple[str, str] = (settings.neo4j_username, settings.neo4j_password.get_secret_value())
    async with AsyncGraphDatabase.driver(URI, auth=AUTH) as driver:
        yield driver

async def get_session(driver: AsyncDriver = Depends(get_driver)) -> AsyncGenerator[None, None]:
    async with driver.session(database=settings.neo4j_db_name) as session:
        yield session

neo4jSession = Annotated[Session, Depends(get_session)]