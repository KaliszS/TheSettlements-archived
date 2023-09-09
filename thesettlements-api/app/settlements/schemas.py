from uuid import UUID

from pydantic import BaseModel, Field

from app.structures.schemas import Structure


class SettlementBase(BaseModel):
    name: str
    x: int
    y: int
    population: int | None = 100
    structures: list[Structure] | None = Field(default_factory=list)
    owner: UUID | None = None
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    x: int
    y: int
    population: int = 100
    structures: list[Structure] = []
    owner: PyObjectId | None = Field(default_factory=PyObjectId)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Roma",
                "x": 0,
                "y": 0,
                "population": 1000,
                "owner": "1",
            }
        }


class SettlementUpdate(SettlementBase):
    name: str | None = None
    population: int | None = None
    structures: list[Structure] | None = None
