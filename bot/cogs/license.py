import discord
from discord import app_commands
from discord.ext import commands

from bot.services.discord_api import api_get


class License(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="licenses", description="View your licenses")
    async def licenses(self, interaction: discord.Interaction):
        discord_id = interaction.user.id
        licenses = await api_get(f"/discord/users/{discord_id}/licenses")
        if not licenses:
            embed = discord.Embed(
                title="Your Licenses",
                description="You have no licenses.",
                color=discord.Color.green(),
            )
        else:
            embed = discord.Embed(title="Your Licenses", color=discord.Color.green())
            for lic in licenses:
                embed.add_field(
                    name=lic["product_name"],
                    value=f"Status: {lic['status']}\nExpires: {lic.get('expires_at', 'Never')}",
                    inline=False,
                )
        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(License(bot))
