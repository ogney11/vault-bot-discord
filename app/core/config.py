from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Vault"
    api_prefix: str = "/api/v1"
    database_url: str = "postgresql+asyncpg://vault:vault@localhost:5432/vault"
    redis_url: str = "redis://localhost:6379/0"
    debug: bool = False

    secret_key: str = "change-me"
    access_token_expire_minutes: int = 60 * 24

    stripe_secret_key: str = ""
    stripe_webhook_secret: str = ""

    discord_client_id: str = ""
    discord_client_secret: str = ""
    discord_bot_token: str = ""

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
