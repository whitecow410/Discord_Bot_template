import discord
from discord.ext import commands
import json
import os
import asyncio

# 讀取 json 檔
with open('setting.json', 'r', encoding='utf8') as file:
    setting = json.load(file)

# 啟用所有 intents
intents = discord.Intents.all()

bot = commands.Bot(command_prefix=setting['PREFIX'], intents=intents)


# 設置 Bot 啟用後的事件
@bot.event
async def on_ready():
    print(f' Logged in as {bot.user}')


# 載入所有cog
async def cogs():
    for filename in os.listdir("cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")


async def main():
    await cogs()
    if __name__ == "__main__":
        await bot.start(setting['TOKEN'])  # -> string

asyncio.run(main())
