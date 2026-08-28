from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from uuid import UUID

from app.db.session import get_db
from app.core.deps import get_workspace_member
from app.models.workspace_member import WorkspaceMember
from app.schemas.license import LicenseActivationRequest, LicenseValidationResponse

router = APIRouter()

@router.post("/activate")
async def activate_license(
    workspace_id: UUID,
    activation_data: LicenseActivationRequest,
    db: Annotated[AsyncSession, Depends(get_db)]
):
    """
    Activate a license (no auth required, public endpoint).
    """
    raise HTTPException(status_code=501, detail="Not implemented")

@router.post("/validate")
async def validate_license(
    workspace_id: UUID,
    validation_data: LicenseActivationRequest,
    db: Annotated[AsyncSession, Depends(get_db)]
) -> LicenseValidationResponse:
    """
    Validate a license (no auth required, public endpoint).
    """
    raise HTTPException(status_code=501, detail="Not implemented")
