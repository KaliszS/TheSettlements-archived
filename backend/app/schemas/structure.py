from pydantic import BaseModel

class Structure(BaseModel):
    level: int | None = None
    type: str
    cost: int