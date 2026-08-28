import uuid
from sqlalchemy import String, ForeignKey, Index, Text, Boolean, DateTime
from app.db.uuid import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base
from app.models.mixins import TimestampMixin
from datetime import datetime

class ProductVersion(Base, TimestampMixin):
    __tablename__ = "product_versions"
    __table_args__ = (Index("ix_product_versions_product_id", "product_id"),)

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    version: Mapped[str] = mapped_column(String(50), nullable=False)
    changelog: Mapped[str | None] = mapped_column(Text, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    product: Mapped["Product"] = relationship(back_populates="versions")
    files: Mapped[list["ProductFile"]] = relationship(back_populates="version")
    downloads: Mapped[list["Download"]] = relationship(back_populates="version")
