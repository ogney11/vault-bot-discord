from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Annotated
from uuid import UUID

from app.db.session import get_db
from app.core.deps import get_current_user, get_workspace_admin, get_workspace_member
from app.models.user import User
from app.models.workspace import Workspace
from app.models.workspace_member import WorkspaceMember
from app.schemas.workspace import WorkspaceCreate, WorkspaceUpdate, WorkspaceResponse

router = APIRouter()

@router.post("/", response_model=WorkspaceResponse)
async def create_workspace(
    workspace_data: WorkspaceCreate,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[AsyncSession, Depends(get_db)]
):
    """
    Create a new workspace.
    """
    raise HTTPException(status_code=501, detail="Not implemented")

@router.get("/{workspace_id}", response_model=WorkspaceResponse)
async def get_workspace(
    workspace_id: UUID,
    member: Annotated[WorkspaceMember, Depends(get_workspace_member)],
    db: Annotated[AsyncSession, Depends(get_db)]
):
    """
    Get workspace details.
    """
    raise HTTPException(status_code=501, detail="Not implemented")

@router.put("/{workspace_id}", response_model=WorkspaceResponse)
async def update_workspace(
    workspace_id: UUID,
    workspace_data: WorkspaceUpdate,
    admin: Annotated[WorkspaceMember, Depends(get_workspace_admin)],
    db: Annotated[AsyncSession, Depends(get_db)]
):
    """
    Update workspace (admin only).
    """
    raise HTTPException(status_code=501, detail="Not implemented")
