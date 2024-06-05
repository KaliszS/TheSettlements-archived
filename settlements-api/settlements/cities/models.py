from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from settlements.database import Base
from settlements.models import primary_key, int32


class Settlement(Base):
    id: Mapped[primary_key(UUID)]
    name: Mapped[str]
    coord_x: Mapped[int]
    coord_y: Mapped[int]
    population: Mapped[int32]
    structures: Mapped[list[int]]
    resources: Mapped[list[int32]]
    units: Mapped[list[int32]]
    campaign_id: Mapped[UUID] = mapped_column(ForeignKey("games_campaign.id"))
    player_id: Mapped[UUID | None] = mapped_column(ForeignKey("games_player.id"))


class Resource(Base):
    id: Mapped[primary_key(int)]
    name: Mapped[str]


class ConstructionInfo(Base):
    id: Mapped[primary_key(int)]
    name: Mapped[str]

    levels: Mapped[list["Construction"]] = relationship(backref="construction_info")


class Construction(Base):
    id: Mapped[primary_key(int)] = mapped_column(ForeignKey("cities_constructioninfo.id"))
    level: Mapped[primary_key(int)]
    construction_time: Mapped[int]
    cost: Mapped[list[int32]]
    population_upkeep: Mapped[int32]
