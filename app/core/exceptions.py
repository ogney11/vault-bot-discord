class VaultException(Exception):
    def __init__(self, status_code: int = 500, detail: str = "Internal Server Error"):
        self.status_code = status_code
        self.detail = detail
        super().__init__(detail)


class UnauthorizedException(VaultException):
    def __init__(self, detail: str = "Not authenticated"):
        super().__init__(status_code=401, detail=detail)


class ForbiddenException(VaultException):
    def __init__(self, detail: str = "Forbidden"):
        super().__init__(status_code=403, detail=detail)


class NotFoundException(VaultException):
    def __init__(self, detail: str = "Not found"):
        super().__init__(status_code=404, detail=detail)


class ConflictException(VaultException):
    def __init__(self, detail: str = "Conflict"):
        super().__init__(status_code=409, detail=detail)
