import discord
from discord.ext import commands
import json
from core.classes import Cog_Extension

with open("setting.json",mode="r",encoding="utf-8") as jfile:
    jdata=json.load(jfile)
    

class Pic(Cog_Extension):
    #與Main類別一樣Pic直接繼承Cog_Extension的屬性
    #如此一來便能更方便的更動內容

    @commands.command()
    async def pity(self, ctx): #pity -- 可憐
        pic = discord.File(jdata['摳蓮'])
        await ctx.send(file= pic)
    
    @commands.command()
    async def wad(self, ctx): #wad -- What a disaster
        pic = discord.File(jdata['桂圈爭亂'])
        await ctx.send(file= pic)

    @commands.command()
    async def iml(self, ctx): #iml -- I'm listening
        pic = discord.File(jdata['沒關西你繼續掰'])
        await ctx.send(file= pic)

    @commands.command()
    async def okay(self, ctx): 
        pic = discord.File(jdata['還要繼續敷衍嗎'])
        await ctx.send(file= pic)

    @commands.command()
    async def yktm(self, ctx): #yktm -- You konw too much
        pic = discord.File(jdata['你知道的太多了'])
        await ctx.send(file= pic)

    @commands.command()
    async def omg(self, ctx): 
        pic = discord.File(jdata['下薯我了'])
        await ctx.send(file= pic)

    @commands.command()
    async def ty(self, ctx): #ty -- Thank you
        pic = discord.File(jdata['感謝'])
        await ctx.send(file= pic)

    @commands.command()
    async def hungry(self, ctx):
        pic = discord.File(jdata['腦子有動'])
        await ctx.send(file= pic)

    @commands.command()
    async def bobobo(self, ctx):
        pic = discord.File(jdata['很會打發喔'])
        await ctx.send(file= pic)

    @commands.command()
    async def yw(self, ctx): #yw -- You win
        pic = discord.File(jdata['輸給你了'])
        await ctx.send(file= pic)

    @commands.command()
    async def tf(self, ctx): #tf -- Too fast
        pic = discord.File(jdata['2fast'])
        await ctx.send(file= pic)

def setup(bot):
    bot.add_cog(Pic(bot))