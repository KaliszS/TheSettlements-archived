from pydantic import BaseModel


class StructureBase(BaseModel):
    level: int | None = None
    type: str
    cost: int
