# HoverDive Copyright 2021 By Zan4eg#5557
# Импорты библиотек

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

PREFIX = '.' # Переменная префикса

Bot = commands.Bot( command_prefix = PREFIX ) # Установка префикса бота
@Bot.remove_command('help') #Удаление стандартной комманды help

def get_random_string(length):
	letters = string.ascii_letters + string.digits
	result_str = ''.join(random.choice(letters) for i in range(length))
	return result_str

# При загрузке бота
@Bot.event
async def on_ready():
    activity = discord.Game(name = "HoverDive | .help", url='https://twitch.com/zan4egpayne')
    await Bot.change_presence( status = discord.Status.online, activity = activity )
    print("Logged in as HoverDive!")
    print("HoverDive Copyright 2021 By Zan4eg#5557")
    print("Бот запущен и готов к работе!")
    while True:
        await asyncio.sleep(8)
        await Bot.change_presence( status = discord.Status.online, activity = discord.Game(name = ".help | HoverDive") )
        await asyncio.sleep(8)
        await Bot.change_presence( status = discord.Status.online, activity = discord.Game(name = "Бот создан Zan4eg#5557") )

@Bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		await ctx.send(embed = discord.Embed(description = f'{ctx.author.name}, команда не найдена!', colour = discord.Color.red()))

@Bot.command( pass_context=True )
async def news( ctx, *, news = None):
    if ctx.message.author.guild_permissions.administrator:
        channel = Bot.get_channel(896670930787504129)
        emb=discord.Embed( title = '', colour= 0x04ff00 )
        emb.set_author(name=ctx.author.name + "#" + ctx.author.discriminator + ", запостил новость!", icon_url = ctx.author.avatar_url)
        emb.add_field( name = 'Текст новости:', value = '** ```{}``` **'.format( news ) )
        emb.set_image(url="https://media.discordapp.net/attachments/685812932415717402/899200236529020948/news.png?width=1440&height=480")
        emb.set_footer(text= "© HoverDive 💚 | Новости")
        emb.timestamp = datetime.datetime.utcnow()
        await ctx.send('@everyone')
        message = await channel.send(embed=emb)
        await message.add_reaction('✅')
        await message.add_reaction('❌')
        await ctx.message.delete()
    else:
        await ctx.send(":cross: | У вас нет прав!")

@Bot.command()
async def admins( ctx ):
    emb=discord.Embed( title = '', colour= 0x04ff00 )
    emb.add_field( name = 'Админы:', value = '\n <:zan4eg:899245316463804436>ㆍ[Zan4egus](https://www.youtube.com/channel/UCGujlBSRsD51PBETG39CczQ) \n \n <:notis:899245278698299402>ㆍ[Бафик](https://www.youtube.com/channel/UCiZdhc2Hb-hPfJd5vEDvVWA)')
    emb.set_footer(text= "© HoverDive 💚 | Админы")
    emb.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=emb)

@Bot.event
async def on_message(message):
    await Bot.process_commands(message)
    channel = message.channel
    support_channel = Bot.get_channel(899661397959516241)
    isBot = message.author.bot
    if(message.author.bot): return
    if(channel != support_channel): return
    await message.delete()
    guild = message.guild
    await channel.set_permissions(message.author, read_messages=True,send_messages=False)
    emb=discord.Embed( title = '', colour= 0x04ff00 )
    emb.set_author(name="Вайтлист")
    emb.set_footer(text=f"{message.author.display_name}", icon_url = message.author.avatar_url)
    emb.add_field( name = 'Ник на добавление:', value = '`{}`'.format(message.content) )
    await channel.send(embed=emb)
    await message.author.edit(nick='{}'.format(message.author.display_name) + ' ({})'.format(message.content))
    #message2 = await channel.send(message.author.mention + ", вы успешно оставили своё обращение! Перейдите в канал " + channel2.mention + " для просмотра ответа.")
    await asyncio.sleep(5)

token = os.environ.get('BOT_TOKEN')
Bot.run( str(token) )
