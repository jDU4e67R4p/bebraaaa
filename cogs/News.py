import discord
import random
from discord.ext import commands
import asyncio
import socket
import smtplib
import datetime
import pyowm
import json
from datetime import timedelta
import os
from Cybernator import Paginator as pag
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json, socket, threading, time, concurrent.futures
from six.moves import urllib
from random import choice
import string
import requests
import pyshorteners

class News(commands.Cog):

    def __init__(self, Bot):
        self.Bot = Bot

    @commands.command()
    async def news(self, ctx, *, news = None):
        if ctx.message.author.guild_permissions.administrator:
            channel = self.Bot.get_channel(896670930787504129)
            emb=discord.Embed( title = '', colour= 0x04ff00 )
            emb.set_author(name=ctx.author.name + "#" + ctx.author.discriminator + ", запостил новость!", icon_url = ctx.author.avatar_url)
            emb.add_field( name = 'Текст новости:', value = '** ```{}``` **'.format( news ) )
            emb.set_image(url="https://media.discordapp.net/attachments/685812932415717402/899200236529020948/news.png?width=1440&height=480")
            emb.set_footer(text= "© HoverDive 💚 | Новости")
            emb.timestamp = datetime.datetime.utcnow()
            await channel.send('@everyone')
            message = await channel.send(embed=emb)
            await message.add_reaction('✅')
            await message.add_reaction('❌')
            await ctx.message.delete()
        else:
            await ctx.send(":cross: | У вас нет прав!")

def setup(Bot):
	Bot.add_cog(News(Bot))