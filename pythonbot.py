import discord
import os
#import settings
#from discord.ext.commands import Bot
#from discord.ext import commands

bot = discord.Client() #Initialise Client
#bot = commands.Bot(command_prefix = os.environ["prefix"])

# TODO: Once ready
@bot.event
async def on_ready():
    print("Bot is online and connected to Discord")

# TODO: When a message is sent on discord
@bot.event
async def on_message(message):
    if message.author.bot:
        return #ignore other bots

    if "hello" in message.content.lower():
        await  bot.send_message(message.channel, "Hello! :)")
    if "cookie" in message.content.lower():
        await bot.send_message(message.channel, ":cookie:")

bot.run(os.environ["token"])
#bot.run(settings.getToken())
