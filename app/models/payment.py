import uuid
from sqlalchemy import String, BigInteger, ForeignKey, Index, DateTime, JSON
from app.db.uuid import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base
from app.models.mixins import TimestampMixin

class Payment(Base, TimestampMixin):
    __tablename__ = "payments"
    __table_args__ = (
        Index("ix_payments_order_id", "order_id"),
        Index("ix_payments_vault_subscription_id", "vault_subscription_id"),
        Index("ix_payments_stripe_payment_intent_id", "stripe_payment_intent_id"),
    )

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    workspace_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("workspaces.id", ondelete="CASCADE"), nullable=False)
    order_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey("orders.id", ondelete="SET NULL"), nullable=True)
    vault_subscription_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey("vault_subscriptions.id", ondelete="SET NULL"), nullable=True)
    stripe_payment_intent_id: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    amount_minor: Mapped[int] = mapped_column(BigInteger, nullable=False)
    currency: Mapped[str] = mapped_column(String(3), nullable=False)
    status: Mapped[str] = mapped_column(String(30), nullable=False)
    refunded_amount_minor: Mapped[int] = mapped_column(BigInteger, default=0, nullable=False)
    fee_minor: Mapped[int] = mapped_column(BigInteger, default=0, nullable=False)
    metadata_json: Mapped[dict] = mapped_column("metadata", JSON, default=dict, nullable=False)

    workspace: Mapped["Workspace"] = relationship()
    order: Mapped["Order"] = relationship(back_populates="payments")
    vault_subscription: Mapped["VaultSubscription"] = relationship(back_populates="payments")
