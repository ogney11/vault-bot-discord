from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from uuid import UUID

from app.db.session import get_db
from app.core.deps import get_workspace_member
from app.models.workspace_member import WorkspaceMember
from app.schemas.order import OrderCreate, OrderResponse

router = APIRouter()

@router.post("/", response_model=OrderResponse)
async def create_order(
    workspace_id: UUID,
    order_data: OrderCreate,
    member: Annotated[WorkspaceMember, Depends(get_workspace_member)],
    db: Annotated[AsyncSession, Depends(get_db)]
):
    """
    Create an order (customer or admin).
    """
    raise HTTPException(status_code=501, detail="Not implemented")

@router.get("/{order_id}", response_model=OrderResponse)
async def get_order(
    workspace_id: UUID,
    order_id: UUID,
    member: Annotated[WorkspaceMember, Depends(get_workspace_member)],
    db: Annotated[AsyncSession, Depends(get_db)]
):
    """
    Get order details.
    """
    raise HTTPException(status_code=501, detail="Not implemented")
