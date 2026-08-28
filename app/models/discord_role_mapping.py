import uuid
from sqlalchemy import BigInteger, String, ForeignKey, Index, Boolean, JSON
from app.db.uuid import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base
from app.models.mixins import TimestampMixin

class DiscordRoleMapping(Base, TimestampMixin):
    __tablename__ = "discord_role_mappings"
    __table_args__ = (
        Index("ix_discord_role_mappings_workspace_id", "workspace_id"),
        Index("ix_discord_role_mappings_guild_role", "guild_id", "role_id"),
    )

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    workspace_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("workspaces.id", ondelete="CASCADE"), nullable=False)
    guild_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    role_id: Mapped[str] = mapped_column(String(100), nullable=False)
    resource_type: Mapped[str] = mapped_column(String(50), nullable=False)
    resource_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), nullable=True)
    action: Mapped[str] = mapped_column(String(20), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    metadata_json: Mapped[dict] = mapped_column("metadata", JSON, default=dict, nullable=False)

    workspace: Mapped["Workspace"] = relationship(back_populates="role_mappings")
