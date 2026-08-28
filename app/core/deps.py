from app.core.exceptions import UnauthorizedException, ForbiddenException


def get_current_user():
    raise UnauthorizedException(detail="Not authenticated")


def get_workspace_member():
    raise ForbiddenException(detail="Not a workspace member")


def get_workspace_admin():
    raise ForbiddenException(detail="Not a workspace admin")
