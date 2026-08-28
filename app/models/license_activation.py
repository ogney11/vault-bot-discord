import uuid
from sqlalchemy import String, ForeignKey, Index, DateTime, func
from app.db.uuid import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base
from app.models.mixins import TimestampMixin
from datetime import datetime

class LicenseActivation(Base, TimestampMixin):
    __tablename__ = "license_activations"
    __table_args__ = (
        Index("ix_license_activations_license_id", "license_id"),
        Index("ix_license_activations_device_id", "license_id", "device_id", unique=True),
    )

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    license_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("licenses.id", ondelete="CASCADE"), nullable=False)
    device_id: Mapped[str] = mapped_column(String(255), nullable=False)
    ip_address: Mapped[str | None] = mapped_column(String(45), nullable=True)
    user_agent: Mapped[str | None] = mapped_column(String(500), nullable=True)
    activated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    deactivated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    license: Mapped["License"] = relationship(back_populates="activations")
