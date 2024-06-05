from typing import Annotated, Iterator
from uuid import UUID

from fastapi import Depends
from sqlalchemy import create_engine, DateTime, String, Engine, inspect
from sqlalchemy.orm import DeclarativeBase, declared_attr, Session, sessionmaker
from sqlalchemy.dialects.postgresql import SMALLINT, INTEGER, BOOLEAN, ARRAY, UUID as pgUUID

from settlements.config import settings
from settlements.models import int32, datetime_tz


engine = create_engine(settings.database_uri, pool_pre_ping=True)


def prepare_sessionmaker(engine: Engine) -> sessionmaker:
    return sessionmaker(autocommit=False, bind=engine)


def resolve_table_name(module: str, name: str) -> str:
    """
    Resolve table name from app and model names.
    """
    modules = module.split(".")
    app_name = ""
    for module_name in modules:
        if module_name == "models":
            break
        app_name = module_name

    if not app_name:
        raise ModuleNotFoundError("Database tables must be defined in modules called `models`.")

    return "_".join([app_name, name.lower()])


class Base(DeclarativeBase):
    @declared_attr
    def __tablename__(self) -> str:
        return resolve_table_name(self.__module__, self.__name__)

    @property
    def id_str(self) -> str:
        return f"{inspect(self).identity[0]}"

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(id={self.id_str})>"

    type_annotation_map = {
        str: String,
        bool: BOOLEAN,
        int: SMALLINT,
        int32: INTEGER,
        UUID: pgUUID,
        list[int]: ARRAY(SMALLINT),
        list[int32]: ARRAY(INTEGER),
        datetime_tz: DateTime(timezone=True),
    }


def get_db() -> Iterator[Session]:
    db = prepare_sessionmaker(engine)()
    with db:
        yield db


DbSession = Annotated[Session, Depends(get_db)]
