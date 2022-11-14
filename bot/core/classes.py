import discord
from discord.ext import commands


class Cog_Basic_Inherit(commands.Cog):
    # 讓 Cog 繼承基本屬性
    def __init__(self, bot):
        self.bot = bot
