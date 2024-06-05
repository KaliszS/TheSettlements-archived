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


class ResourceCreate(BaseModel):
    id: int
    name: str


class ResourceRead(ResourceCreate):
    pass


class ResourceUpdate(BaseModel):
    name: str | None = None


class ConstructionInfoCreate(BaseModel):
    id: int
    name: str


class ConstructionInfoRead(ConstructionInfoCreate):
    pass


class ConstructionInfoUpdate(BaseModel):
    name: str | None = None


class ConstructionCreate(BaseModel):
    id: int
    level: int | None = 1
    construction_time: int
    cost: list[int]
    population_upkeep: int


class ConstructionRead(BaseModel):
    id: int
    level: int
    construction_time: int
    cost: list[int]
    population_upkeep: int


class ConstructionUpdate(BaseModel):
    level: int | None = None
    construction_time: int | None = None
    cost: list[int] | None = None
    population_upkeep: int | None = None
