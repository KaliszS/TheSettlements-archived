from typing import Optional
from pydantic import BaseModel

class Tournament(BaseModel):
    name: str
    tag: str
    teams: Optional[dict] = None


class Player(BaseModel):
    nickname: str
    gid: str
    team: str


class Relationship(BaseModel):
    relationship_type: str
    soure_node: Player
    target_node: Player
    properties: Optional[dict] = None


class Query(BaseModel):
    response: list
