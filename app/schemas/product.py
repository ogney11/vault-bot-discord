from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class ProductCreate(BaseModel):
    name: str
    slug: str
    description: str | None = None
    price_minor: int
    currency: str = "USD"
    image_url: str | None = None
    discord_role_id: str | None = None

class ProductUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    price_minor: int | None = None
    is_active: bool | None = None

class ProductResponse(BaseModel):
    id: UUID
    workspace_id: UUID
    name: str
    slug: str
    description: str | None
    price_minor: int
    currency: str
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
