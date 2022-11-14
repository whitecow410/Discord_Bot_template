import discord
from discord.ext import commands
from core.classes import Cog_Basic_Inherit


class Event(Cog_Basic_Inherit):

    # 關鍵字觸發事件
    @commands.Cog.listener()
    async def on_message(self, message):
        # 無事所有由 Bot 發出的訊息
        if message.author.bot:
            return

        # 檢測關鍵字
        if message.content.startswith("apple"):
            await message.channel.send("apple !")

    # 設置指令錯誤事件
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"可愛的參數不見了! QAQ")


async def setup(bot):
    await bot.add_cog(Event(bot))
