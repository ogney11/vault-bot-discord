from pydantic_settings import BaseSettings

class BotSettings(BaseSettings):
    api_base_url: str = "http://localhost:8000/api/v1"
    discord_bot_token: str = ""

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

bot_settings = BotSettings()
