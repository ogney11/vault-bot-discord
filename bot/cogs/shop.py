import discord
from discord import app_commands
from discord.ext import commands

from bot.services.discord_api import api_get


class Shop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="shop", description="Browse all available products")
    async def shop(self, interaction: discord.Interaction):
        guild_id = interaction.guild.id if interaction.guild else None
        products = await api_get(f"/discord/guilds/{guild_id}/products") if guild_id else []
        if not products:
            embed = discord.Embed(
                title="Vault Shop",
                description="No products available.",
                color=discord.Color.blue(),
            )
        else:
            embed = discord.Embed(
                title="Vault Shop",
                description="Available products:",
                color=discord.Color.blue(),
            )
            for p in products:
                embed.add_field(
                    name=p["name"],
                    value=f"{p['price_minor']/100:.2f} {p['currency']}",
                    inline=False,
                )
        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(Shop(bot))
