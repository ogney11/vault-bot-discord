from fastapi import APIRouter
from app.api.v1 import auth, users, workspaces, products, customers, orders, licenses
from app.api.v1 import downloads, subscriptions, payments, api_keys, audit, discord

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(workspaces.router, prefix="/workspaces", tags=["workspaces"])
api_router.include_router(products.router, prefix="/products", tags=["products"])
api_router.include_router(customers.router, prefix="/customers", tags=["customers"])
api_router.include_router(orders.router, prefix="/orders", tags=["orders"])
api_router.include_router(licenses.router, prefix="/licenses", tags=["licenses"])
api_router.include_router(downloads.router, prefix="/downloads", tags=["downloads"])
api_router.include_router(subscriptions.router, prefix="/subscriptions", tags=["subscriptions"])
api_router.include_router(payments.router, prefix="/payments", tags=["payments"])
api_router.include_router(api_keys.router, prefix="/api-keys", tags=["api-keys"])
api_router.include_router(audit.router, prefix="/audit", tags=["audit"])
api_router.include_router(discord.router, prefix="/discord", tags=["discord"])

__all__ = ["api_router"]
