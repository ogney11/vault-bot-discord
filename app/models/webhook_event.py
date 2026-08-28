import uuid
from sqlalchemy import String, DateTime, JSON
from app.db.uuid import UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base
from app.models.mixins import TimestampMixin
from datetime import datetime

class WebhookEvent(Base, TimestampMixin):
    __tablename__ = "webhook_events"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    stripe_event_id: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    event_type: Mapped[str] = mapped_column(String(100), nullable=False)
    payload: Mapped[dict] = mapped_column(JSON, nullable=False)
    processed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    error: Mapped[str | None] = mapped_column(String(500), nullable=True)
