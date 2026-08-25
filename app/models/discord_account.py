import uuid
from sqlalchemy import String, BigInteger, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base
from app.models.mixins import TimestampMixin
from datetime import datetime

class DiscordAccount(Base, TimestampMixin):
    __tablename__ = "discord_accounts"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    discord_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
    username: Mapped[str] = mapped_column(String(100), nullable=False)
    discriminator: Mapped[str | None] = mapped_column(String(10), nullable=True)
    avatar: Mapped[str | None] = mapped_column(String(255), nullable=True)
    access_token_enc: Mapped[str] = mapped_column(String(500), nullable=False)  # encrypted
    refresh_token_enc: Mapped[str] = mapped_column(String(500), nullable=False)  # encrypted
    expires_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    user: Mapped["User"] = relationship(back_populates="discord_account")
