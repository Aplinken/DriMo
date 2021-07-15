import discord
from discord.ext import commands
import youtube_dl
import os

class Music(commands.Cog):
	def __init__(self,client):
		self.client = client

	@commands.command()
	async def play(self,ctx,url:str):
		if ctx.author.voice is None:
			await ctx.send('You need to be connected to a Voice Channel first!')
			return
		else:
			channel = ctx.author.voice.channel.name
		song_present = os.path.isfile('song.mp3')
		try:
			if song_present:
				os.remove('song.mp3')
		except PermissionError:
			await ctx.send("Wait for the current song to finish or Manually Stop the song using the Stop command")
			return



		vc = discord.utils.get(ctx.guild.voice_channels,name=channel)
		try:
			await vc.connect()
		except:
			pass
		voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
		await yt_dwnld(url=url)
		voice.play(discord.FFmpegPCMAudio('song.mp3'))
				

	@commands.command()
	async def leave(self,ctx):
		voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
		if not voice is None:
			if voice.is_connected:
				await voice.disconnect()
			else:
				await ctx.send('The Bot is not connected to any voice channel')
		else:
			await ctx.send('The Bot is not connected to any voice channel')

	@commands.command()
	async def pause(self,ctx):
		voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
		if voice.is_playing():
			voice.pause()
		else:
			await ctx.send('Nothing Seems To be playing')

	@commands.command()
	async def resume(self,ctx):
		voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
		if voice.is_paused():
			voice.resume()
		else:
			await ctx.send('I still hear music')


	@commands.command()
	async def stop(self,ctx):
		voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
		voice.stop()


async def yt_dwnld(url):
	ytdl_opts = {'format':'bestaudio/best',
				'postprocessors':[{
				'key':'FFmpegExtractAudio',
				'preferredcodec':'mp3',
				'preferredquality':'192'
				}]}

	with youtube_dl.YoutubeDL(ytdl_opts) as ydl:
		ydl.download([url])
	for file in os.listdir("./"):
		if file.endswith(".mp3"):
			os.rename(file, 'song.mp3')	

def setup(client):
	client.add_cog(Music(client))