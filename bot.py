import os

import discord
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, welcome to my Discord server!')


@client.event
async def on_message(message):
    if ('<@972208992283660348>' in message.content) and ('hello' in message.content):
        await message.reply("Hello, How can I help you?", mention_author = True)
        
        

#async def on_message(message):
#    if "botA01 hello" in message.content.lower():
#        await message.channel.send('Hello Boss, I am here to help you')
#    elif "Hello Boss, I am here to help you" in message.content.lower():
#        return    
#bot = commands.Bot(command_prefix='!')
#@client.event
#async def on_message(message):
#    if f'hello {bot.user.name}' in message.content.lower():
#        await message.channel.send('Happy Birthday Aman Singh! 🎈🎉')
#    elif message.author == client.user:
#       return

client.run("OTcyMjA4OTkyMjgzNjYwMzQ4.GTnr1t.9VguCntJ-PG5fuXNdP5FXiAHoKiOcup9YyRHag")
