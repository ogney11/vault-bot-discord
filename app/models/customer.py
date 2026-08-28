import uuid
from sqlalchemy import String, BigInteger, ForeignKey, Index
from app.db.uuid import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base
from app.models.mixins import TimestampMixin

class Customer(Base, TimestampMixin):
    __tablename__ = "customers"
    __table_args__ = (
        Index("ix_customers_workspace_discord", "workspace_id", "discord_id"),
        Index("ix_customers_workspace_email", "workspace_id", "email"),
    )

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    workspace_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("workspaces.id", ondelete="CASCADE"), nullable=False)
    user_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    discord_id: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    email: Mapped[str | None] = mapped_column(String(255), nullable=True)
    stripe_customer_id: Mapped[str | None] = mapped_column(String(255), nullable=True)
    name: Mapped[str | None] = mapped_column(String(255), nullable=True)

    workspace: Mapped["Workspace"] = relationship(back_populates="customers")
    user: Mapped["User"] = relationship()
    orders: Mapped[list["Order"]] = relationship(back_populates="customer")
    licenses: Mapped[list["License"]] = relationship(back_populates="customer")
    downloads: Mapped[list["Download"]] = relationship(back_populates="customer")
