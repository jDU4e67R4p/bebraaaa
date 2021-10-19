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
    async def on_member_join(self, member):
        msg = f"{member.name} зашел на сервер."
        await self.bot.get_channel(899215863775895562).send(msg)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        msg = f"{member.name} вышел с сервера."
        await self.bot.get_channel(899215863775895562).send(msg)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        msg = f"Сообщение до изменений {before.content}\n" \
              f"Сообщение после {after.content}"
        await self.bot.get_channel(899980494886813697).send(msg)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        msg = f"Удаленное сообщение: {message.content}\n"
        await self.bot.get_channel(899980494886813697).send(msg)

    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        if before.channel is None:
            msg = f"{member.display_name} зашел в канал {after.channel.mention}"
            await self.bot.get_channel(899980494886813697).send(msg)
        elif after.channel is None:
            msg = f"{member.display_name} покинул канал {before.channel.mention}"
            await self.bot.get_channel(899980494886813697).send(msg)
        elif before.channel != after.channel:
            msg = f"{member.display_name} перешел из канала {before.channel.mention} в канал {after.channel.mention}"
            await self.bot.get_channel(899980494886813697).send(msg)

def setup(Bot):
	Bot.add_cog(WhiteCheck(Bot))
