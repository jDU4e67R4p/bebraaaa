import json
import requests
import discord
from discord.ext import commands

class YouTube(commands.Cog):

    def __init__(self, Bot):
        self.Bot = Bot

    @commands.command()
    async def watch(self, ctx):
        data = {
            "max_age": 86400,
            "max_uses": 0,
            "target_application_id": 755600276941176913,
            "target_type": 2,
            "temporary": False,
            "validate": None
        }
        headers = {
            "Authorization": "Bot NzI0Njk5OTkyMTk5MDA0Mjgx.XvD_dg.pp9cElvrDY-_ca3ddOxTWhV_t3A",
            "Content-Type": "application/json"
        }
        if ctx.author.voice is not None:
            if ctx.author.voice.channel is not None:
                channel = ctx.author.voice.channel.id
            else:
                await ctx.send("> Зайдите в канал.")
        else:
            await ctx.send("> Зайдите в канал.")

        response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites", data=json.dumps(data), headers=headers)
        link = json.loads(response.content)

        await ctx.send(f"> Ваше активити создано. Подключайтесь по ссылке: \n https://discord.com/invite/{link['code']}")

def setup(Bot):
    Bot.add_cog(YouTube(Bot))