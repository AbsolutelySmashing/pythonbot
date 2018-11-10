import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client() #Initialise Client 
client = commands.Bot(command_prefix = "!") #Initialise client bot

@client.event 
async def on_ready():
    print("Bot is online and connected to Discord") #This will be called when the bot connects to the server

@client.event
async def on_message(message):
    if message.content == "cookie":
        await message.channel.send(":cookie:") #responds with Cookie emoji when someone says "cookie"

client.run("NTEwNzcwNzIxMTYxNDc4MTQ5.DshM6A.mwx57Kl-lLqOOQBLQbHmlUN3Ho4")
