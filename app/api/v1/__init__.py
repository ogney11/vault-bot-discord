from fastapi import APIRouter
from app.api.v1.endpoints import auth, workspaces, products, orders, licenses, downloads

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(workspaces.router, prefix="/workspaces", tags=["workspaces"])
api_router.include_router(products.router, prefix="/products", tags=["products"])
api_router.include_router(orders.router, prefix="/orders", tags=["orders"])
api_router.include_router(licenses.router, prefix="/licenses", tags=["licenses"])
api_router.include_router(downloads.router, prefix="/downloads", tags=["downloads"])

__all__ = ["api_router"]
