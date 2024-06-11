from uuid import UUID
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from settlements.database import Base
from settlements.models import primary_key

if TYPE_CHECKING:  # resolves circular imports
    from settlements import Player


class User(Base):
    id: Mapped[primary_key(UUID)]
    name: Mapped[str]
    password: Mapped[str]
    is_active: Mapped[bool]
    is_superuser: Mapped[bool]

    players: Mapped[list["Player"]] = relationship(backref="user")
