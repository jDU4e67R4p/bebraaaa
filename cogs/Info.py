import json
import requests
import os
import discord
from discord.ext import commands
from mcstatus import MinecraftServer

class Info(commands.Cog):

    def __init__(self, Bot):
        self.Bot = Bot

    @commands.command()
    async def info(self, ctx):
        server = MinecraftServer.lookup("mc.hoverdive.ru")
        status = server.status()
        emb = discord.Embed( title="", colour=0x8721ED ) # Создаем ембед
        emb.add_field( name=':bust_in_silhouette: Онлайн HoverDive', value='Игроков на сервере: ` {0} `'.format(status.players.online) )
        await ctx.send( embed = emb )

def setup(Bot):
    Bot.add_cog(Info(Bot))
