import aiohttp
import discord
from discord.ext import commands
import io
from util import getEmbed

class Tools(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="3dsrngtool")
    async def grab3dsrngtool(self, ctx):
        embed = getEmbed("3DSRNGTool Releases", "https://github.com/wwwwwwzx/3DSRNGTool/releases")
        await ctx.channel.send(embed=embed)
        await self.bot.log_channel.send(f"{ctx.author.mention} ran command .3dsrngtool in {ctx.channel.mention}")

    @commands.command(name="pokefinder")
    async def grabPokeFinder(self, ctx):
        embed = getEmbed("PokeFinder Releases", "https://github.com/Admiral-Fish/PokeFinder/releases")
        await ctx.channel.send(embed=embed)        
        await self.bot.log_channel.send(f"{ctx.author.mention} ran command .pokefinder in {ctx.channel.mention}")

    @commands.command(name="rngreporter")
    async def grabRNGReporter(self, ctx):
        embed = getEmbed("RNG Reporter Releases", "https://github.com/Admiral-Fish/RNGReporter/releases")
        await ctx.channel.send(embed=embed)
        await self.bot.log_channel.send(f"{ctx.author.mention} ran command .rngreporter in {ctx.channel.mention}")

    @commands.command()
    async def installpcalc(self, ctx):
        embed = getEmbed("Guide to Installing PCalc", "https://pokemonrng.com/guides/tools/en/How%20to%20Install%20PCalc.md")
        await ctx.channel.send(embed=embed)
        await self.bot.log_channel.send(f"{ctx.author.mention} ran command .installpcalc in {ctx.channel.mention}")

    @commands.command()
    async def pcalc(self, ctx, build):
        if ctx.channel.id not in self.bot.build_channels:
            embed = getEmbed("Uh oh!", "Please do not ask for PCalc in this channel.")
            await ctx.channel.send(embed=embed)
            return

        if build not in self.bot.build_list:
            embed = getEmbed("Uh oh!", "Build not found! Please try: usum, sm, oras, xy, tport")
            await ctx.channel.send(embed=embed)
            return

        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://pokemonrng.com/downloads/pcalc/pcalc-{build}.zip") as resp:
                if resp.status != 200:
                    return await ctx.channel.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.channel.send(content=f"Here's the latest PCalc-usum", file=discord.File(data, f"pcalc-{build}.zip"))                
                await self.bot.log_channel.send(f"{ctx.author.mention} ran command .pcalc in {ctx.channel.mention}")

    @commands.command()
    async def fixntr(self, ctx):
        message = "\n".join([
        "Delete the following files from the SD card to do a clean install:",
        "\t /ntr.o3ds/bin",
        "\t /ntr.n3ds.bin",
        "\t /3ds/bootntr",
        "\t /3ds/ntr",
        "\t /Nintendo 3DS/EBNTR",
        "\n Reinstall [BootNTR Selector](https://github.com/Nanquitas/BootNTR/releases)." 
        ])

        embed = getEmbed("Fixing NTR", message)
        await ctx.channel.send(embed=embed)        
        await self.bot.log_channel.send(f"{ctx.author.mention} ran command .fixntr in {ctx.channel.mention}")

def setup(bot):
    bot.add_cog(Tools(bot))