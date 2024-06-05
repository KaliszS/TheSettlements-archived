from datetime import datetime
from typing import Annotated

from sqlalchemy.orm import mapped_column


int32 = Annotated[int, ...]
datetime_tz = Annotated[datetime, True]


def primary_key[T](T, default=None) -> Annotated:
    return Annotated[T, mapped_column(primary_key=True, default=default)]


def index[T](T) -> Annotated:
    return Annotated[T, mapped_column(index=True)]
