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
import mctools
from mctools import RCONClient

class Rcon(commands.Cog):

    def __init__(self, Bot):
        self.Bot = Bot

    @commands.Cog.listener()
    async def on_message(self, message):
    	channel = message.channel
    	support_channel = self.Bot.get_channel(899661397959516241)
    	isBot = message.author.bot
    	if(message.author.bot): return
    	if(channel != support_channel): return

    	HOST = '135.181.170.86'
    	PORT = 25730

    	rcon = RCONClient(HOST, port=PORT)
    	if rcon.login("QaRhO1209"):
    		resp = rcon.command("easywl add {}".format(message.content))
    		resp = rcon.command("bc &7На сервер был добавлен новый игрок под ником &b{}".format(message.content))
    		rcon.stop()

def setup(Bot):
	Bot.add_cog(Rcon(Bot))