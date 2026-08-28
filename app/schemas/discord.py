from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class DiscordAccountResponse(BaseModel):
    id: UUID
    discord_id: int
    username: str
    avatar: str | None
    created_at: datetime

    class Config:
        from_attributes = True
