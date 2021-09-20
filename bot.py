import discord
from discord.ext import commands
import json
import random, os, asyncio

with open("setting.json",mode="r",encoding="utf-8") as jfile:
    jdata=json.load(jfile)
    #開啟setting.json並讀取內容 方便之後直接取出預先設定好的資料

bot = commands.Bot(command_prefix="..")

@bot.event 
async def on_ready():
    print("_N7's puppet is online_")

@bot.command() #help
async def h(ctx):
    await ctx.send(
    """`Need help?            
Go ask somebody else! 
I'm just a puppet     `"""
    )

@bot.command() #Load-Cog
async def load(ctx, extension): #ctx=context 偵測上下文屬性
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'{extension} have been load')

@bot.command() #Unload-Cog
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'{extension} have been unload')

@bot.command() #Reload-Cog
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'{extension} have been reload')

for filename in os.listdir('./cmds'): #列出所有路境內所有文件名稱 ./為相對路徑
    if filename.endswith('.py'): #篩選出.py檔案
        bot.load_extension(f'cmds.{filename[:-3]}') 
        #如同form...import 資料夾.副檔名 [:-3]去掉後面三個字(.py)
        #ex. cmd.classes.py -> cmd.classes

if __name__ =="__main__":
    bot.run(jdata["Token"])