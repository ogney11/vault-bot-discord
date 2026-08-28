from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from uuid import UUID

from app.db.session import get_db
from app.schemas.download import DownloadTokenRequest, DownloadTokenResponse

router = APIRouter()

@router.post("/token")
async def create_download_token(
    workspace_id: UUID,
    token_request: DownloadTokenRequest,
    db: Annotated[AsyncSession, Depends(get_db)]
) -> DownloadTokenResponse:
    """
    Create a download token (requires auth).
    """
    raise HTTPException(status_code=501, detail="Not implemented")

@router.get("/file/{token}")
async def download_file(
    workspace_id: UUID,
    token: str,
    db: Annotated[AsyncSession, Depends(get_db)]
):
    """
    Download a file using a download token (no auth required).
    """
    raise HTTPException(status_code=501, detail="Not implemented")
