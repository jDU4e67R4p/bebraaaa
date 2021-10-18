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

class Main(commands.Cog):

	def __init__(self, Bot):
		self.Bot = Bot

	@commands.Cog.listener()
	async def on_ready(self):
		activity = discord.Game(name = "HoverDive | Created by Zan4eg#5557", url='https://twitch.com/zan4egpayne')
		await self.Bot.change_presence( status = discord.Status.online, activity = activity )
		print("Logged in as HoverDive!")
		print("HoverDive Copyright 2021 By Zan4eg#5557")
		print("Бот запущен и готов к работе!")

def setup(Bot):
	Bot.add_cog(Main(Bot))
