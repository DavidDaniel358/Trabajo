####bot_logic

import random
import requests

def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "HEADS"
    else:
        return "TAILS"


def ecologico():
    consejo = "Utiliza las botellas para hecer macetas"
    codigo = "Utiliza el carton para hacer estanterias"
    clase = random.randint(0, 2)
    if clase == 0:
        return consejo
    else:
        return codigo
####bot.py

import os
import random
import discord
from bot_logic import gen_pass
from discord.ext import commands
from bot_logic import flip_coin

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix = "$", intents=intents )

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def flip(ctx):     
    await ctx.send(flip_coin)

bot.run ("Token")

####boteco_teen

import discord
from discord.ext import commands
from bot_logic import ecologico

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = "/", intents=intents )

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def ecogarden(ctx):  
    await ctx.send(ecologico)

bot.run("Token")
