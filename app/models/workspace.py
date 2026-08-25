import uuid
from sqlalchemy import String, Boolean, BigInteger, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base
from app.models.mixins import TimestampMixin

class Workspace(Base, TimestampMixin):
    __tablename__ = "workspaces"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    owner_user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="RESTRICT"), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    slug: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    discord_guild_id: Mapped[int | None] = mapped_column(BigInteger, unique=True, nullable=True)
    is_claimed: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    owner: Mapped["User"] = relationship()
    members: Mapped[list["WorkspaceMember"]] = relationship(back_populates="workspace")
    products: Mapped[list["Product"]] = relationship(back_populates="workspace")
    customers: Mapped[list["Customer"]] = relationship(back_populates="workspace")
    orders: Mapped[list["Order"]] = relationship(back_populates="workspace")
    licenses: Mapped[list["License"]] = relationship(back_populates="workspace")
    vault_subscriptions: Mapped[list["VaultSubscription"]] = relationship(back_populates="workspace")
    api_keys: Mapped[list["ApiKey"]] = relationship(back_populates="workspace")
    audit_logs: Mapped[list["AuditLog"]] = relationship(back_populates="workspace")
    role_mappings: Mapped[list["DiscordRoleMapping"]] = relationship(back_populates="workspace")
