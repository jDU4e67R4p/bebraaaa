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

Bot = commands.Bot(command_prefix = ".")
Bot.remove_command("help")

Bot.load_extension('cogs.Admins')
Bot.load_extension('cogs.main')
Bot.load_extension('cogs.News')
Bot.load_extension('cogs.WhiteCheck')
Bot.load_extension('cogs.Rcon')
Bot.load_extension('cogs.RconCommand')
Bot.load_extension('cogs.YouTube')
Bot.load_extension('cogs.Info')
Bot.load_extension('cogs.music')

@Bot.command()
async def load(ctx, extension):
	if ctx.author.id == 287220642053357569:
		Bot.load_extension(f"cogs.{extension}")
		await ctx.send("```Коги загружены...```")
	else:
		await ctx.send("```Вы не разработчик бота...```")

@Bot.command()
async def unload(ctx, extension):
	if ctx.author.id == 287220642053357569:
		Bot.unload_extension(f"cogs.{extension}")
		await ctx.send("```Коги выружены...```")
	else:
		await ctx.send("```Вы не разработчик бота...```")

@Bot.command()
async def reload(ctx, extension):
	if ctx.author.id == 287220642053357569:
		Bot.unload_extension(f"cogs.{extension}")
		Bot.load_extension(f"cogs.{extension}")
		await ctx.send("```Коги перезагружены...```")
	else:
		await ctx.send("```Вы не разработчик бота...```")

token = os.environ.get('BOT_TOKEN')
Bot.run( str(token) )
