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

class Admins(commands.Cog):

    def __init__(self, Bot):
        self.Bot = Bot

    @commands.command()
    async def admins(self, ctx):
        emb=discord.Embed( title = '', colour= 0x04ff00 )
        emb.add_field( name = 'Админы:', value = '\n <:zan4eg:899245316463804436>ㆍ[Zan4egus](https://www.youtube.com/channel/UCGujlBSRsD51PBETG39CczQ) \n \n <:notis:899245278698299402>ㆍ[Бафик](https://www.youtube.com/channel/UCiZdhc2Hb-hPfJd5vEDvVWA)')
        emb.set_footer(text= "© HoverDive 💚 | Админы")
        emb.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=emb)

def setup(Bot):
	Bot.add_cog(Admins(Bot))