from uuid import UUID

from fastapi import APIRouter, status

from settlements.database import DbSession
from settlements.cities.schemas import SettlementCreate, SettlementRead, SettlementUpdate
from settlements.cities.services import settlement_services


router = APIRouter()


@router.post("", response_model=SettlementRead, status_code=status.HTTP_201_CREATED)
async def create_settlement(db: DbSession, settlement: SettlementCreate):
    return await settlement_services.create(db, settlement)


@router.get("/{settlement_id}", response_model=SettlementRead, status_code=status.HTTP_200_OK)
async def read_settlement(db: DbSession, settlement_id: UUID):
    return await settlement_services.get(db, settlement_id)


@router.patch("/{settlement_id}", response_model=SettlementRead, status_code=status.HTTP_200_OK)
async def update_settlement(db: DbSession, settlement_id: UUID, settlement: SettlementUpdate):
    return await settlement_services.update(db, settlement_id, settlement)


@router.delete("/{settlement_id}", response_model=SettlementRead, status_code=status.HTTP_200_OK)
async def delete_settlement(db: DbSession, settlement_id: UUID):
    return await settlement_services.delete(db, settlement_id)
