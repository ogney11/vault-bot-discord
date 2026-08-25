from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class LicenseActivationRequest(BaseModel):
    license_key: str
    product_slug: str
    device_id: str

class LicenseValidationResponse(BaseModel):
    valid: bool
    reason: str | None = None
    activation_count: int | None = None
    max_activations: int | None = None
    expires_at: datetime | None = None
