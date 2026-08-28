import discord
from discord.ext import commands
from bot.services.discord_api import api_get

class License(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="licenses", description="View your licenses")
    async def licenses(self, ctx):
        # Assume the API can look up licenses by Discord user ID
        discord_id = ctx.author.id
        licenses = await api_get(f"/discord/users/{discord_id}/licenses")
        if not licenses:
            embed = discord.Embed(
                title="Your Licenses",
                description="You have no licenses.",
                color=discord.Color.green()
            )
        else:
            embed = discord.Embed(
                title="Your Licenses",
                color=discord.Color.green()
            )
            for lic in licenses:
                embed.add_field(
                    name=lic["product_name"],
                    value=f"Status: {lic['status']}\nExpires: {lic.get('expires_at', 'Never')}",
                    inline=False
                )
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(License(bot))
