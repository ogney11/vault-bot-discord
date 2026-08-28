import uuid
from sqlalchemy import String, BigInteger, ForeignKey, Index, CheckConstraint, DateTime, Integer
from app.db.uuid import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base
from app.models.mixins import TimestampMixin
from datetime import datetime

class License(Base, TimestampMixin):
    __tablename__ = "licenses"
    __table_args__ = (
        Index("ix_licenses_workspace_id", "workspace_id"),
        Index("ix_licenses_customer_id", "customer_id"),
        Index("ix_licenses_product_id", "product_id"),
        Index("ix_licenses_license_hash", "license_hash"),
        CheckConstraint("max_activations >= 0", name="ck_license_max_activations_non_negative"),
    )

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    workspace_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("workspaces.id", ondelete="CASCADE"), nullable=False)
    customer_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("customers.id", ondelete="RESTRICT"), nullable=False)
    product_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("products.id", ondelete="RESTRICT"), nullable=False)
    license_hash: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)
    license_prefix: Mapped[str] = mapped_column(String(20), nullable=False)
    status: Mapped[str] = mapped_column(String(20), default="active", nullable=False)
    expires_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    max_activations: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    activation_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    revoked_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    revoked_reason: Mapped[str | None] = mapped_column(String(255), nullable=True)

    workspace: Mapped["Workspace"] = relationship(back_populates="licenses")
    customer: Mapped["Customer"] = relationship(back_populates="licenses")
    product: Mapped["Product"] = relationship(back_populates="licenses")
    activations: Mapped[list["LicenseActivation"]] = relationship(back_populates="license")
