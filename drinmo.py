import discord
from discord.ext import commands
import json
import os
import random
import time
import jishaku

os.chdir("E:\\Drinmo")
ownerid = 513374271460868106

# Client created
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=commands.when_mentioned_or('~'), case_insensitive=True)
client.remove_command("help")

#Starting Defaults

@client.event
async def on_ready():
	await client.change_presence(activity=discord.Game(name="In Early Stages of Development"))

@client.command()
async def load(ctx, extension):
	if ctx.author.id == ownerid:
		client.load_extension(f'cogs.{extension}')
		await ctx.send(f'{extension} has been loaded!')
	else:
		return False

@client.command()
async def unload(ctx, extension):
	if ctx.author.id == ownerid:
		client.unload_extension(f'cogs.{extension}')
		await ctx.send(f'{extension} has been unloaded!')
	else:
		return False

@client.command()
async def reload(ctx, extension):
	if ctx.author.id == ownerid:
		client.reload_extension(f'cogs.{extension}')
		await ctx.send(f'{extension} has been reloaded!')
	else:
		return False

#Info Command

@client.command()
async def info(ctx):
	myEmbed = discord.Embed(title="DriMo", color=0x00ff00)
	myEmbed.add_field(name="Version:", value="v0.4.1", inline=True)
	myEmbed.add_field(name="Created by:", value="Aplinken", inline=True)
	myEmbed.set_footer(text="Promoted by the motherland of degeneratia")
		
	await ctx.channel.send(embed=myEmbed)


#Finishing Touch


for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')

client.load_extension('jishaku')


with open('token.txt') as f:
	token = f.read()
client.run(token)