import pytest


@pytest.fixture
def client():
    from app.main import app
    from httpx import ASGITransport, AsyncClient
    import asyncio

    transport = ASGITransport(app=app)

    async def inner():
        async with AsyncClient(transport=transport, base_url="http://test") as ac:
            return ac

    return inner
