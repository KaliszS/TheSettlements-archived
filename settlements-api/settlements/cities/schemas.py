from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class SettlementCreate(BaseModel):
    id: UUID | None = Field(default_factory=uuid4)
    name: str
    coord_x: int
    coord_y: int
    population: int
    structures: list[int] = Field(default_factory=list)
    resources: list[int] = Field(default_factory=list)
    units: list[int] = Field(default_factory=list)
    campaign_id: UUID
    player_id: UUID | None = None


class SettlementRead(BaseModel):
    id: UUID
    name: str
    coord_x: int
    coord_y: int
    population: int
    structures: list[int]
    resources: list[int]
    units: list[int]
    campaign_id: UUID
    player_id: UUID | None = None


class SettlementUpdate(BaseModel):
    name: str | None = None
    coord_x: int | None = None
    coord_y: int | None = None
    population: int | None = None
    structures: list[int] | None = None
    resources: list[int] | None = None
    units: list[int] | None = None
    player_id: UUID | None = None
