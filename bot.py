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
import textwrap
from contextlib import redirect_stdout
import traceback
import string
import io
import os

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

def cleanup_code(content):
    if content.startswith('```') and content.endswith('```'):
        return '\n'.join(content.split('\n')[1:-1])
    return content.strip('` \n')

@Bot.command(hidden=True)
@commands.is_owner()
async def eval(ctx, *, code):
    async with ctx.channel.typing():
        env = {
            'bot': Bot,
            'ctx': ctx,
            'channel': ctx.channel,
            'author': ctx.author,
            'guild': ctx.guild,
            'message': ctx.message,
            }
        env.update(globals())
        code = cleanup_code(code)
        to_compile = f'async def func():\n{textwrap.indent(code, "  ")}'
        stdout = io.StringIO()
        try:
            exec(to_compile, env)
        except Exception as e:
            embed = discord.Embed(title='Error!', description=f'```py\n{e.__class__.__name__}: {e}\n```',
                                    color=0xeb4034)
            return await ctx.send(embed=embed)
        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception as e:
            value = stdout.getvalue()
            embed = discord.Embed(title='Error!', description=f'```py\n{value} {e} {traceback.format_exc()}\n```',
                                    color=0xeb4034)
            return await ctx.send(embed=embed)
        else:
            value = stdout.getvalue()
            if ret is None:
                if value:
                    embed = discord.Embed(title='Exec result:', description=f'```py\n{value[:1990]}\n```')
                else:
                    embed = discord.Embed(title='Eval code executed!')
            else:
                value = stdout.getvalue()
                embed = discord.Embed(title='Exec result:', description=f'```py\n{value}{ret}\n```')

    await ctx.send(embed=embed)

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
