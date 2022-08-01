from fastapi import APIRouter, Body
from typing import List, Optional
from app.utils.db import neo4j_driver
from app.utils.schema import Tournament

router = APIRouter()

@router.get("/", response_model=List[Tournament])
async def get_all_tournaments():
    cypher = (
        f"MATCH (t: Tournament) RETURN t"
    )

    with neo4j_driver.session() as session:
        result = session.run(query=cypher)
        data = result.data()

    return [list(d.values())[0] for d in data]

@router.post("/create", response_model=Tournament)
async def create_tournament(tournament: Tournament):
    cypher = (
        f"CREATE (t: Tournament {{"
        f"name: '{tournament.name}', tag: '{tournament.tag}'"
        f"}}) RETURN t.name AS name, t.tag AS tag"
    )

    with neo4j_driver.session() as session:
        result = session.run(query=cypher)
        data = result.data()[0]

    return Tournament(
        name=data["name"], tag=data["tag"], teams={}
    )
