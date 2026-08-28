import uuid

from sqlalchemy import String
from sqlalchemy.types import TypeDecorator


class UUID(TypeDecorator):
    """A MySQL-compatible UUID column backed by CHAR(36)."""

    impl = String(36)
    cache_ok = True

    def __init__(self, as_uuid: bool = False, *args, **kwargs):
        self.as_uuid = as_uuid
        super().__init__(*args, **kwargs)

    @property
    def python_type(self):
        return uuid.UUID

    def process_bind_param(self, value, dialect):
        if value is None:
            return None
        return str(value)

    def process_result_value(self, value, dialect):
        if value is None:
            return None
        return uuid.UUID(value)
