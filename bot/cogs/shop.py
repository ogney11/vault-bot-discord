import discord
from discord.ext import commands
from bot.services.api import api_get

class Shop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="shop", description="Browse all available products")
    async def shop(self, ctx):
        # Fetch products from the API for this guild
        guild_id = ctx.guild.id
        products = await api_get(f"/discord/guilds/{guild_id}/products")
        if not products:
            embed = discord.Embed(
                title="Vault Shop",
                description="No products available.",
                color=discord.Color.blue()
            )
        else:
            embed = discord.Embed(
                title="Vault Shop",
                description="Available products:",
                color=discord.Color.blue()
            )
            for p in products:
                embed.add_field(
                    name=p["name"],
                    value=f"{p['price_minor']/100:.2f} {p['currency']}",
                    inline=False
                )
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Shop(bot))
