from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class OrderCreate(BaseModel):
    customer_id: UUID
    items: list[dict]

class OrderResponse(BaseModel):
    id: UUID
    workspace_id: UUID
    customer_id: UUID
    order_number: str
    status: str
    payment_status: str
    total_minor: int
    currency: str
    created_at: datetime

    class Config:
        from_attributes = True
