# bot.py

import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
#GUILD = os.getenv("DISCORD_GUILD")

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)

    print(f'{client.user} has connected to Discord server {guild.name} (id: {guild.id})')

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    response = "FYL Bing Bong"

    if message.content == "!bb":
        await message.channel.send(repsonse)

client.run(TOKEN)

