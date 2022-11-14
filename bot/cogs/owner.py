import discord
from discord.ext import commands
from core.classes import Cog_Basic_Inherit
import os


class Owner(Cog_Basic_Inherit):

    @commands.is_owner()
    @commands.command(description="關閉機器人", aliases=["down"], hidden=True)
    async def shutdown(self, ctx: commands.Context):
        await ctx.send(f"已關閉 {self.bot.user.mention}")
        await self.bot.close()

    @commands.is_owner()
    @commands.command(description="加載模塊", aliases=["lo"], hidden=True)
    async def load(self, ctx: commands.Context, extension: str):
        await self.bot.load_extension(f"cogs.{extension}")
        await ctx.send(f"已加載 `cogs.{extension}`")

    @commands.is_owner()
    @commands.command(description="卸載模塊", aliases=["un"], hidden=True)
    async def unload(self, ctx: commands.Context, extension: str):
        await self.bot.unload_extension(f"cogs.{extension}")
        await ctx.send(f"已卸載 `cogs.{extension}`")

    @commands.is_owner()
    @commands.command(description="重新加載模塊", aliases=["re"], hidden=True)
    async def reload(self, ctx: commands.Context, extension: str):
        if extension == "*" or extension == "all":
            for filename in os.listdir("./cogs"):
                if filename.endswith(".py"):
                    await self.bot.reload_extension(f"cogs.{filename[:-3]}")
            await ctx.send("已重新加載 `all extension`")
        else:
            await self.bot.reload_extension(f"cogs.{extension}")
            await ctx.send(f"已重新加載 `cogs.{extension}`")


async def setup(bot):
    await bot.add_cog(Owner(bot))
