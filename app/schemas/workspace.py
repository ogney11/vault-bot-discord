from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class WorkspaceCreate(BaseModel):
    name: str
    slug: str
    discord_guild_id: int | None = None

class WorkspaceUpdate(BaseModel):
    name: str | None = None
    discord_guild_id: int | None = None

class WorkspaceResponse(BaseModel):
    id: UUID
    owner_user_id: UUID
    name: str
    slug: str
    discord_guild_id: int | None
    is_claimed: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
