from typing import Iterator

from neo4j import Driver, GraphDatabase

from .config import settings


def get_driver() -> Iterator[Driver]:
    URI: str = settings.database_uri
    AUTH: tuple[str, str] = (
        settings.neo4j_username,
        settings.neo4j_password.get_secret_value(),
    )
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        yield driver
