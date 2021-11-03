import json
import requests
import os
import discord
from discord.ext import commands
from mcstatus import MinecraftServer
import asyncio

class Info(commands.Cog):

    def __init__(self, Bot):
        self.Bot = Bot

    @commands.command()
    async def info(self, ctx):
        server = MinecraftServer.lookup("mc.hoverdive.ru")
        status = server.status()
        emb = discord.Embed( title="", colour=0x8721ED ) # Создаем ембед
        emb.add_field( name='<:player:904740455885963274> Онлайн HoverDive', value='Игроков на сервере: ` {0} `'.format(status.players.online) )
        await ctx.send( embed = emb )

    @commands.command(pass_context=True)
    async def servers(self, ctx):
        if ctx.message.author.guild_permissions.administrator:
            while True:
                await ctx.channel.purge(limit=1)
                server = MinecraftServer.lookup("mc.hoverdive.ru")
                status = server.status()
                emb = discord.Embed( title="Статистика Minecraft сервера HoverDive", colour=0x940ba7 )
                emb.add_field(name='Название сервера', value='HoverDive', inline=True)
                emb.add_field(name='Статус сервера', value='<:tick:899206743186354196> Онлайн', inline=True)
                emb.add_field(name='Игроков', value='<:player:904740455885963274> {0}'.format(status.players.online), inline=True)
                emb.set_thumbnail(url='https://media.discordapp.net/attachments/685812932415717402/899203964996812820/ava.png?width=678&height=678')
                emb.set_footer(text='Обновление информации каждые 3 минуты.')
                msg = await ctx.send(embed=emb)
                await asyncio.sleep(180)
        else:
            await ctx.send('> У вас не прав администратора')

def setup(Bot):
    Bot.add_cog(Info(Bot))
