from discord import *
import discord
from discord.ext import commands
import random
from mcstatus import MinecraftServer
import requests
from cogs.resources.config import settings as bot_cfg
import datetime
from discord_components import DiscordComponents, Button, ButtonStyle
from threading import Thread
import asyncio
import sqlite3
import pymysql
#db = sqlite3.connect('./db/users.sqlite')

db = pymysql.connect(
        host='mysql3.joinserver.ru',
        port=3306,
        user='u59079_vKyrNuI8Uc',
        password='OYAHxIFnEmyB30suPSr86Cyd',
        database='s59079_reallyworld',
        cursorclass=pymysql.cursors.DictCursor
    )
cursor = db.cursor()

db3 = sqlite3.connect('./db/mutes.sqlite')
cursor3 = db3.cursor()


def get_perms(member):
    try:
        cursor.execute(f'SELECT plvlperms FROM userscfg WHERE id = {member.id}')
        return int(cursor.fetchone()[0])
    except:
        return 0

def set_perms(member, lvl):
    cursor.execute(f'SELECT * FROM userscfg WHERE id = {member.id}')
    if len(cursor.fetchall()) <= 0:
        cursor.execute(f'INSERT INTO userscfg VALUES({member.id},0,{lvl},0,0,0)')
        db.commit()
    else:
        cursor.execute(f'UPDATE userscfg SET plvlperms = {lvl} WHERE id = {member.id}')
        db.commit()


def get_points(member):
    cursor.execute(f'SELECT * FROM userscfg WHERE id = {member.id}')
    if len(cursor.fetchall()) <= 0:
        return 0
    else:
        cursor.execute(f'SELECT ppoints FROM userscfg WHERE id = {member.id}')
        return int(cursor.fetchone()[0])



def get_ywig(member):
    cursor.execute(f'SELECT * FROM userscfg WHERE id = {member.id}')
    if len(cursor.fetchall()) <= 0:
        return 0
    else:
        cursor.execute(f'SELECT pywarns FROM userscfg WHERE id = {member.id}')
        return int(cursor.fetchone()[0])


def get_rwig(member):
    cursor.execute(f'SELECT * FROM userscfg WHERE id = {member.id}')
    if len(cursor.fetchall()) <= 0:
        return 0
    else:
        cursor.execute(f'SELECT prwarns FROM userscfg WHERE id = {member.id}')
        return int(cursor.fetchone()[0])



def get_dolz(member):
    try:
        cursor.execute(f'SELECT plvlperms FROM userscfg WHERE id = {member.id}')
        return f'{cursor.fetchone()[0]}'.replace('1', 'Саппорт').replace(
            '2',
            'Хелпер'
        ).replace('3', 'Ст.Хелпер').replace('4','Мл.Модератор').replace(
            '5',
            'Ст.Модератор'
        ).replace('6', 'Гл.Модератор').replace('7', 'Куратор').replace('8','Администратор').replace(
            '9',
            'Супер пупер вышка'
        )
    except:
        return 'Участник'



def set_points(member, lvl):
    cursor.execute(f'SELECT * FROM userscfg WHERE id = {member.id}')
    if len(cursor.fetchall()) <= 0:
        cursor.execute(f'INSERT INTO userscfg VALUES({member.id},0,0,{lvl},0,0)')
        db.commit()
    else:
        cursor.execute(f'UPDATE userscfg SET ppoints = {lvl} WHERE id = {member.id}')
        db.commit()


def add_points(member, lvl):
    cursor.execute(f'SELECT * FROM userscfg WHERE id = {member.id}')
    if len(cursor.fetchall()) <= 0:
        cursor.execute(f'INSERT INTO userscfg VALUES({member.id},0,0,{lvl + 0},0,0)')
        db.commit()
    else:
        cursor.execute(f'UPDATE userscfg SET ppoints = {lvl + get_points(member)} WHERE id = {member.id}')
        db.commit()




def add_rwig(member):
    cursor.execute(f'SELECT * FROM userscfg WHERE id = {member.id}')
    if len(cursor.fetchall()) <= 0:
        cursor.execute(f'INSERT INTO userscfg VALUES({member.id},0,0,0,0,1)')
        db.commit()
    else:
        cursor.execute(f'UPDATE userscfg SET prwarns = {1 + get_rwig(member)} WHERE id = {member.id}')
        db.commit()



def add_ywig(member):
    cursor.execute(f'SELECT * FROM userscfg WHERE id = {member.id}')
    if len(cursor.fetchall()) <= 0:
        cursor.execute(f'INSERT INTO userscfg VALUES({member.id},0,0,0,1,0)')
        db.commit()
    else:
        cursor.execute(f'UPDATE userscfg SET pywarns = {1 + get_ywig(member)} WHERE id = {member.id}')
        db.commit()


def rem_rwig(member):
    cursor.execute(f'SELECT * FROM userscfg WHERE id = {member.id}')
    if len(cursor.fetchall()) <= 0:
        cursor.execute(f'INSERT INTO userscfg VALUES({member.id},0,0,0,0,0)')
        db.commit()
    else:
        cursor.execute(f'UPDATE userscfg SET prwarns = {get_rwig(member) - 1} WHERE id = {member.id}')
        db.commit()



def rem_ywig(member):
    cursor.execute(f'SELECT * FROM userscfg WHERE id = {member.id}')
    if len(cursor.fetchall()) <= 0:
        cursor.execute(f'INSERT INTO userscfg VALUES({member.id},0,0,0,0,0)')
        db.commit()
    else:
        cursor.execute(f'UPDATE userscfg SET pywarns = {get_ywig(member) - 1} WHERE id = {member.id}')
        db.commit()


def rem_points(member, lvl):
    cursor.execute(f'SELECT * FROM userscfg WHERE id = {member.id}')
    if len(cursor.fetchall()) <= 0:
        cursor.execute(f'INSERT INTO userscfg VALUES({member.id},0,0,0,0,0)')
        db.commit()
    else:
        cursor.execute(f'UPDATE userscfg SET ppoints = {get_points(member) - lvl} WHERE id = {member.id}')
        db.commit()



def set_mute_time(member, timeinsec):
    time = datetime.datetime.now() + datetime.timedelta(seconds=timeinsec)
    cursor3.execute(f'SELECT * FROM mutescfg WHERE id = {member.id}')
    if len(cursor3.fetchall()) <= 0:
        cursor3.execute(f'INSERT INTO mutescfg VALUES({member.id}, "{time.timestamp()}")')
        db3.commit()
        return
    cursor3.execute(f'DELETE FROM mutescfg WHERE id = {member.id}')
    cursor3.execute(f'INSERT INTO mutescfg VALUES({member.id}, "{time.timestamp()}")')
    db3.commit()




async def snyat(member):
    support_role = 828254209933574206
    helper_role = 826150955980030014
    moder_role = 832731097741525002
    stmoder_role = 843486162387075072
    glmod_role = 832731367221231616
    sth_role = 897887981710616778
    kur_role = 804431932262973520
    ryk_role = 740288276686176367

    roles = [ryk_role, kur_role, glmod_role, stmoder_role, moder_role,
    sth_role, helper_role, support_role]
    cursor.execute(f'UPDATE userscfg SET plvlperms = 0 WHERE id = {member.id}')
    cursor.execute(f'UPDATE userscfg SET ppoints = 0 WHERE id = {member.id}')
    cursor.execute(f'UPDATE userscfg SET pywarns = 0 WHERE id = {member.id}')
    cursor.execute(f'UPDATE userscfg SET prwarns = 0 WHERE id = {member.id}')
    db.commit()
    for roleid in roles:
        try:
            role = member.guild.get_role(int(roleid))
            if role in member.roles:
                await member.remove_roles(role)
        except:
            pass
    
