import discord
from discord import app_commands
from discord.ext import commands

from bot.services.discord_api import api_post


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="admin_sync",
        description="Sync workspace with this Discord guild (admin only)",
    )
    @app_commands.default_permissions(administrator=True)
    async def admin_sync(self, interaction: discord.Interaction):
        guild_id = interaction.guild.id if interaction.guild else None
        result = await api_post(f"/discord/guilds/{guild_id}/sync", {})
        if result.get("success"):
            await interaction.response.send_message("Workspace synced successfully!")
        else:
            await interaction.response.send_message("Failed to sync workspace.")

    @app_commands.command(
        name="admin_set_role",
        description="Set role for a product (admin only)",
    )
    @app_commands.default_permissions(administrator=True)
    async def admin_set_role(
        self, interaction: discord.Interaction, product_id: str, role: discord.Role
    ):
        result = await api_post(
            f"/discord/products/{product_id}/role",
            {"role_id": str(role.id)},
        )
        if result.get("success"):
            await interaction.response.send_message(
                f"Role {role.name} set for product."
            )
        else:
            await interaction.response.send_message("Failed to set role.")


async def setup(bot):
    await bot.add_cog(Admin(bot))
