from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class CampaignCreate(BaseModel):
    id: UUID | None = Field(default_factory=uuid4)


class CampaignRead(BaseModel):
    id: UUID


class CampaignUpdate(BaseModel):
    pass


class PlayerCreate(BaseModel):
    id: UUID | None = Field(default_factory=uuid4)
    name: str
    human: bool | None = False
    user_id: UUID | None = None
    campaign_id: UUID


class PlayerRead(BaseModel):
    id: UUID
    name: str
    human: bool
    user_id: UUID | None = None
    campaign_id: UUID


class PlayerUpdate(BaseModel):
    name: str | None = None
    human: bool | None = None
    user_id: UUID | None = None
