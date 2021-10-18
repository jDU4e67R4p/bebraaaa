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

class WhiteCheck(commands.Cog):

    def __init__(self, Bot):
        self.Bot = Bot

    @commands.Cog.listener()
    async def on_message(self, message):
        channel = message.channel
        channel2 = self.Bot.get_channel(899739763018457128)
        support_channel = self.Bot.get_channel(899661397959516241)
        isBot = message.author.bot
        if(message.author.bot): return
        if(channel != support_channel): return
        await message.delete()
        await channel.set_permissions(message.author, read_messages=True,send_messages=False)
        emb=discord.Embed( title = '', colour= 0x04ff00 )
        emb.set_author(name="Вайтлист")
        emb.set_footer(text=f"{message.author.display_name}", icon_url = message.author.avatar_url)
        emb.add_field( name = 'Ник который был добавлен:', value = '`{}`'.format(message.content) )
        await channel.send(embed=emb)
        await channel2.send('easywl add {}'.format(message.content))
        await message.author.edit(nick='{}'.format(message.author.display_name) + ' ({})'.format(message.content))
        await asyncio.sleep(5)
        await self.Bot.process_commands(message)

def setup(Bot):
	Bot.add_cog(WhiteCheck(Bot))