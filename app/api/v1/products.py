from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from uuid import UUID

from app.db.session import get_db
from app.core.deps import get_workspace_admin
from app.models.workspace_member import WorkspaceMember
from app.schemas.product import ProductCreate, ProductUpdate, ProductResponse

router = APIRouter()

@router.post("/", response_model=ProductResponse)
async def create_product(
    workspace_id: UUID,
    product_data: ProductCreate,
    admin: Annotated[WorkspaceMember, Depends(get_workspace_admin)],
    db: Annotated[AsyncSession, Depends(get_db)]
):
    """
    Create a new product (admin only).
    """
    raise HTTPException(status_code=501, detail="Not implemented")

@router.get("/{product_id}", response_model=ProductResponse)
async def get_product(
    workspace_id: UUID,
    product_id: UUID,
    db: Annotated[AsyncSession, Depends(get_db)]
):
    """
    Get product details.
    """
    raise HTTPException(status_code=501, detail="Not implemented")

@router.put("/{product_id}", response_model=ProductResponse)
async def update_product(
    workspace_id: UUID,
    product_id: UUID,
    product_data: ProductUpdate,
    admin: Annotated[WorkspaceMember, Depends(get_workspace_admin)],
    db: Annotated[AsyncSession, Depends(get_db)]
):
    """
    Update product (admin only).
    """
    raise HTTPException(status_code=501, detail="Not implemented")
