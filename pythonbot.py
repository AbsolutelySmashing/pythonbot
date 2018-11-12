import os
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

#Initialise client bot
Client = discord.Client() #Initialise Client 
bot = commands.Bot(command_prefix = os.environ["prefix"]) 

@bot.event 
async def on_ready():
    #This will be called when the bot connects to the server
    print("Bot is online and connected to Discord") 

@bot.event
async def on_message(message):
    #responds with Cookie emoji when someone says "cookie"
    if message.content == "cookie":
        await bot.send_message(message.channel, ":cookie:") 

bot.run(os.environ["token"])
