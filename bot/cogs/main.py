import discord
from discord.ext import commands
from core.classes import Cog_Basic_Inherit
import json

# 讀取 json 檔
with open('setting.json', 'r', encoding='utf8') as file:
    setting = json.load(file)


class Main(Cog_Basic_Inherit):

    @commands.command(description="查看延遲")
    async def ping(self, ctx):
        await ctx.send(f"{round(self.bot.latency*1000)} ms")

    @commands.command(description=f"取得機器人的資訊")
    async def info(self, ctx):
        embed = discord.Embed(
            description=setting['DESCRIPTION'], color=0xffffff)
        embed.set_author(
            name=self.bot.user,
            url="https://discord.gg/bn27V8fJsz",
            icon_url=self.bot.user.display_avatar)
        embed.set_thumbnail(url=self.bot.user.display_avatar)
        embed.add_field(
            name="開發者", value="<@726709068835717140>", inline=False)
        embed.add_field(
            name=f"版本", value=f"{setting['VERSIN']}", inline=True)
        embed.set_footer(text=f"Powered by discord.py v{discord.__version__}")
        embed.timestamp = ctx.message.created_at
        await ctx.send(embed=embed)

    @commands.command(description="訊息複誦")
    async def say(self, ctx: commands.Context, *, message=None):

        # 設置信息標注權限
        mentions = discord.AllowedMentions(
            everyone=False, users=True, roles=False, replied_user=True)

        # 檢查使用者是否有權限標注 @everyone / @here, 如沒有權限設置發出來的信息不會標註
        if "@everyone" in message or "@here" in message:
            if ctx.author.guild_permissions.mention_everyone:
                mentions = discord.AllowedMentions(
                    everyone=True, users=True, roles=True, replied_user=True)

        await ctx.message.delete()
        await ctx.send(message, allowed_mentions=mentions)


async def setup(bot):
    await bot.add_cog(Main(bot))
