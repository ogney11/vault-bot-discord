import uuid
from sqlalchemy import String, BigInteger, ForeignKey, Index, CheckConstraint, DateTime
from app.db.uuid import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base
from app.models.mixins import TimestampMixin
from datetime import datetime

class Order(Base, TimestampMixin):
    __tablename__ = "orders"
    __table_args__ = (
        Index("ix_orders_workspace_id", "workspace_id"),
        Index("ix_orders_customer_id", "customer_id"),
        Index("ix_orders_stripe_payment_intent_id", "stripe_payment_intent_id"),
        CheckConstraint("total_minor >= 0", name="ck_order_total_non_negative"),
    )

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    workspace_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("workspaces.id", ondelete="CASCADE"), nullable=False)
    customer_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("customers.id", ondelete="RESTRICT"), nullable=False)
    order_number: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    idempotency_key: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    status: Mapped[str] = mapped_column(String(30), default="pending", nullable=False)
    payment_status: Mapped[str] = mapped_column(String(30), default="unpaid", nullable=False)
    total_minor: Mapped[int] = mapped_column(BigInteger, nullable=False)
    currency: Mapped[str] = mapped_column(String(3), nullable=False, default="USD")
    stripe_payment_intent_id: Mapped[str | None] = mapped_column(String(255), nullable=True)
    refunded_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    workspace: Mapped["Workspace"] = relationship(back_populates="orders")
    customer: Mapped["Customer"] = relationship(back_populates="orders")
    items: Mapped[list["OrderItem"]] = relationship(back_populates="order")
    payments: Mapped[list["Payment"]] = relationship(back_populates="order")
