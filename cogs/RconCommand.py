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

class RconCommand(commands.Cog):

    def __init__(self, Bot):
        self.Bot = Bot

    @commands.command()
    async def rcon(self, ctx, *, command = None):
        if ctx.message.author.guild_permissions.administrator:
            if command is None:
                await ctx.send("> Вы не указали желаемую команду!")
            else:
                hostheroku = os.environ.get('host')
                portheroku = os.environ.get('port')
                passheroku = os.environ.get('pass')

                HOST = hostheroku
                PORT = portheroku

                rcon = RCONClient(HOST, port=PORT)
                if rcon.login(passheroku):
                    resp = rcon.command("{}".format(command))
                    rcon.stop()

                await ctx.send('> Ваша комманда `{}` успешно была отправлена на сервер.'.format(command))
        else:
            await ctx.send("> У вас нет прав!")

def setup(Bot):
	Bot.add_cog(RconCommand(Bot))