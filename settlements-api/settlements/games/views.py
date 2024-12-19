from uuid import UUID

from fastapi import APIRouter, status

from settlements.database import DbSession
from settlements.games.schemas import (
    CampaignCreate,
    CampaignRead,
    CampaignUpdate,
    PlayerCreate,
    PlayerRead,
    PlayerUpdate,
)
from settlements.games.services import campaign_services, player_services


router = APIRouter()


@router.post("", response_model=CampaignRead, status_code=status.HTTP_201_CREATED)
async def create_campaign(db: DbSession, campaign: CampaignCreate):
    return await campaign_services.create(db, campaign)


@router.get("/{campaign_id}", response_model=CampaignRead, status_code=status.HTTP_200_OK)
async def read_campaign(db: DbSession, campaign_id: UUID):
    return await campaign_services.get(db, campaign_id)


@router.patch("/{campaign_id}", response_model=CampaignRead, status_code=status.HTTP_200_OK)
async def update_campaign(db: DbSession, campaign_id: UUID, campaign: CampaignUpdate):
    return await campaign_services.update(db, campaign_id, campaign)


@router.delete("/{campaign_id}", response_model=CampaignRead, status_code=status.HTTP_200_OK)
async def delete_campaign(db: DbSession, campaign_id: UUID):
    return await campaign_services.delete(db, campaign_id)


@router.post("/{campaign_id}/players", response_model=PlayerRead, status_code=status.HTTP_201_CREATED)
async def create_player(db: DbSession, campaign_id: UUID, player: PlayerCreate):
    player.campaign_id = campaign_id
    return await player_services.create(db, player)


@router.get("/{campaign_id}/players/{player_id}", response_model=PlayerRead, status_code=status.HTTP_200_OK)
async def read_player(db: DbSession, player_id: UUID):
    return await player_services.get(db, player_id)


@router.patch("/{campaign_id}/players/{player_id}", response_model=PlayerRead, status_code=status.HTTP_200_OK)
async def update_player(db: DbSession, player_id: UUID, player: PlayerUpdate):
    return await player_services.update(db, player_id, player)


@router.delete("/{campaign_id}/players/{player_id}", response_model=PlayerRead, status_code=status.HTTP_200_OK)
async def delete_player(db: DbSession, player_id: UUID):
    return await player_services.delete(db, player_id)
