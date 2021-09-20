import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open("setting.json",mode="r",encoding="utf-8") as jfile:
    jdata=json.load(jfile)

class Event(Cog_Extension):

    @commands.Cog.listener() #成員加入訊息
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata["In"]))
        await channel.send(f"{member} 加入了記得簽到喔~")

    @commands.Cog.listener() #成員離開訊息 -- 可能因discord.py版本原因 訊息無法送出
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata["InAndOut"]))
        await channel.send(f"{member} 我們會想念你的")

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content("N7...Are you there?"): #也可使用endswith
            await msg.channel.send("Who is \"N7\"?")
        elif msg.content("N7...Is that you?"):
            await msg.channel.send("Sorry, I'm not the one you\'re looking for. \nBut I'll call you if I see \"N7\".")
        elif msg.content("n( U w U )n"):
            await msg.channel.send("Is that a SAD-emoji?")
        elif msg.content("d( ^ w ^ )b"):
            await msg.channel.send("Is that a HAPPY-emoji?")

def setup(bot):
    bot.add_cog(Event(bot))