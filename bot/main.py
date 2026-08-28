import asyncio

import discord
from discord.ext import commands

from bot.config import bot_settings
from bot.cogs.shop import Shop
from bot.cogs.license import License
from bot.cogs.admin import Admin

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


async def setup():
    await bot.add_cog(Shop(bot))
    await bot.add_cog(License(bot))
    await bot.add_cog(Admin(bot))


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (id: {bot.user.id})")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} slash command(s)")
    except Exception as exc:
        print(f"Failed to sync slash commands: {exc}")


async def main():
    await setup()
    await bot.start(bot_settings.discord_bot_token)


if __name__ == "__main__":
    asyncio.run(main())
