import os
import random
import discord
import sqlite_prod

from discord.ext import commands
from dotenv import load_dotenv

database = '6ft_over.db'



load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")


bot = commands.Bot(command_prefix='!')

@bot.command(name='d6', help='Rolls a 6 sided die and returns the result')
async def d6_roll(ctx):
	dice = [
		str(random.choice(range(1,7)))
	]
	await ctx.send(f'The roll was a **{dice[0]}**')

@bot.command(name='create-channel', help='Creates a new text channel (you must be an Admin to do this)')
@commands.has_role('Admin')
async def create_channel(ctx, channel_name):
	guild = ctx.guild
	existing_channel = discord.utils.get(guild.channels, name=channel_name)
	if not existing_channel:
		print(f'Creating a new channel: {channel_name}')
		await guild.create_text_channel(channel_name)
		await ctx.send(f'New text channel **{channel_name}** was created')

@bot.command(name='scoreboard', help='Displays the Minecraft Deaths Scoreboard')
async def scoreboard(ctx):

	conn = sqlite_prod.create_connection(database)

	scoreboard = sqlite_prod.scoreboard(conn)

	output_text = '\n'.join((line) for line in scoreboard)

	await ctx.send(f"```{output_text}```")

	

@bot.command(name='death', help='Adds a death to the Minecraft Deaths Scoreboard')
async def death(ctx, name):
	
	conn = sqlite_prod.create_connection(database)

	update = sqlite_prod.update_row(conn, name)

	await ctx.send(update)


@bot.command(name='fyl')
async def fyl(ctx):

	await ctx.send('Bing Bong')

	
		
	

bot.run(TOKEN)