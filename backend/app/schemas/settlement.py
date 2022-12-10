from pydantic import BaseModel, Field
from bson import ObjectId

from app.utils.mongo_utils import PyObjectId

class Settlement(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    x: int
    y: int
    population: int
    owner: PyObjectId | None = Field(default_factory=PyObjectId)
       
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = { ObjectId: str }
        schema_extra = {
            "example": {
                "name": "Roma",
                "x": 0,
                "y": 0,
                "population": 1000,
                "owner": "1",
            }
        }

class SettlementUpdate(BaseModel):
    name: str | None
    population: int | None
    owner: PyObjectId | None

    class Config:
        schema_extra = {
            "example": {
                "name": "Roma",
                "population": 1000,
                "owner": "1",
            }
        }

