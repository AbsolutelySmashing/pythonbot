import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

#Initialise client bot
Client = discord.Client() #Initialise Client 
bot = commands.Bot(process.env.prefix) 
bot.run(process.env.token)

@client.event 
async def on_ready():
    #This will be called when the bot connects to the server
    print("Bot is online and connected to Discord") 

@client.event
async def on_message(message):
    #responds with Cookie emoji when someone says "cookie"
    if message.content == "cookie":
        await message.channel.send(":cookie:") 
