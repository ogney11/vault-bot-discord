from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Annotated

from app.db.session import get_db
from app.models.user import User
from app.models.discord_account import DiscordAccount
from app.core.security import create_access_token, hash_token, generate_secure_token, encrypt_data
from app.schemas.user import UserResponse
from app.core.config import settings

router = APIRouter()

class DiscordOAuthRequest:
    code: str
    state: str | None = None

@router.post("/discord/callback")
async def discord_callback(
    code: str,
    state: str | None = None,
    db: Annotated[AsyncSession, Depends(get_db)] = None
):
    """
    Handle Discord OAuth callback.
    Exchange authorization code for access token.
    """
    # This is a placeholder - implement Discord OAuth flow
    raise HTTPException(status_code=501, detail="Not implemented")

@router.post("/logout")
async def logout(
    db: Annotated[AsyncSession, Depends(get_db)] = None
):
    """
    Logout the current user by revoking their session.
    """
    raise HTTPException(status_code=501, detail="Not implemented")

@router.get("/me", response_model=UserResponse)
async def get_current_user_info(
    db: Annotated[AsyncSession, Depends(get_db)] = None
):
    """
    Get current authenticated user info.
    """
    raise HTTPException(status_code=501, detail="Not implemented")
