from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class DownloadTokenRequest(BaseModel):
    customer_id: UUID
    version_id: UUID
    file_id: UUID

class DownloadTokenResponse(BaseModel):
    token: str
    expires_at: datetime
    file_name: str
    size_bytes: int
