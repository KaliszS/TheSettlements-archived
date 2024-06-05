from uuid import UUID
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from settlements.database import Base
from settlements.models import primary_key


if TYPE_CHECKING:  # resolves circular imports
    from settlements import Settlement


class Campaign(Base):
    id: Mapped[primary_key(UUID)]

    players: Mapped[list["Player"]] = relationship(backref="campaign")
    settlements: Mapped[list["Settlement"]] = relationship(backref="campaign")


class Player(Base):
    id: Mapped[primary_key(UUID)]
    name: Mapped[str]
    human: Mapped[bool]
    user_id: Mapped[UUID | None] = mapped_column(ForeignKey("users_user.id"))
    campaign_id: Mapped[UUID] = mapped_column(ForeignKey("games_campaign.id"))

    settlements: Mapped[list["Settlement"]] = relationship(backref="player")
