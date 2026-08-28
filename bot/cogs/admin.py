import discord
from discord.ext import commands
from bot.services.api import api_post

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="admin_sync", description="Sync workspace with this Discord guild (admin only)")
    @commands.has_permissions(administrator=True)
    async def admin_sync(self, ctx):
        guild_id = ctx.guild.id
        # Call API to create/update workspace mapping
        result = await api_post(f"/discord/guilds/{guild_id}/sync", {})
        if result.get("success"):
            await ctx.respond("Workspace synced successfully!")
        else:
            await ctx.respond("Failed to sync workspace.")

    @commands.slash_command(name="admin_set_role", description="Set role for a product (admin only)")
    @commands.has_permissions(administrator=True)
    async def admin_set_role(self, ctx, product_id: str, role: discord.Role):
        # Call API to set Discord role for product
        result = await api_post(
            f"/discord/products/{product_id}/role",
            {"role_id": str(role.id)}
        )
        if result.get("success"):
            await ctx.respond(f"Role {role.name} set for product.")
        else:
            await ctx.respond("Failed to set role.")

def setup(bot):
    bot.add_cog(Admin(bot))
