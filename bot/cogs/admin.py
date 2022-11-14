import discord
from discord.ext import commands
from core.classes import Cog_Basic_Inherit


class Admin(Cog_Basic_Inherit):

    # 設定所需權限
    @commands.has_permissions(manage_messages=True)
    @commands.command(description="訊息清除", aliases=["purge", "delete", "clean"])
    async def clear(self, ctx, amount=int):
        deleted = await ctx.channel.purge(limit=amount+1)
        await ctx.send(f"已清除 {len(deleted-1)}/{amount} 則訊息", delete_after=5)

    @commands.has_permissions(kick_members=True)
    @commands.command(description="把成員踢出")
    async def kick(self, ctx, member: discord.Member = None, *, reason="沒有原因"):
        await member.kick(reason=f"{ctx.author}：{reason}")
        await ctx.send(f"{ctx.author.mention} 已踢出 {member.mention}**\n原因：`{reason}")


async def setup(bot):
    await bot.add_cog(Admin(bot))
