import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension): 
    #Main類別直接繼承Cog_Extension的屬性
    #如此一來便能更方便的更動內容

    @commands.command() #ping指令
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}(ms)') 
 
    @commands.command() #臨時用來鬧鬧其他成員的指令 -- 對話
    async def speak(ctx): 
        await ctx.send('Yeeee')

def setup(bot): #將bot傳入setup
    bot.add_cog(Main(bot)) #新增cog(Main)傳入bot