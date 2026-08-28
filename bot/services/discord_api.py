import httpx
from bot.config import bot_settings

async def api_get(path: str) -> dict | list:
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{bot_settings.api_base_url}{path}")
        resp.raise_for_status()
        return resp.json()

async def api_post(path: str, data: dict) -> dict:
    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{bot_settings.api_base_url}{path}", json=data)
        resp.raise_for_status()
        return resp.json()
