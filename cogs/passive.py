import discord
from discord.ext import commands

class Passive(commands.Cog):
	def __init__(self,client):
		self.client = client


	#Help Command Stuff

	@commands.group(invoke_without_command=True,case_insensitive=True)
	async def help(self,ctx):
		em = discord.Embed(title="Help",description="Use the ~help <command> for extended help",color=discord.Color.green())

		em.add_field(name="Fun", value="`Meme`,`8ball`,`Kickinthenuts`")
		em.add_field(name="Music", value="`Play`,`Resume`,`Stop`,`Pause`,`Leave`")
		em.add_field(name="Misc", value="`Info`")

		await ctx.send(embed=em)

	@help.command()
	async def info(self,ctx):

		em = discord.Embed(title="Info",description="Shows Information of the bot",color=discord.Color.green())
		em.add_field(name="**Syntax**", value="~info")
		await ctx.send(embed=em)

	@help.command(aliases=['8ball'])
	async def _8ball(self,ctx):

		em = discord.Embed(title="8ball",description="It's 8 ball kid",color=discord.Color.green())
		em.add_field(name="**Syntax**", value="~8ball")
		await ctx.send(embed=em)

	@help.command()
	async def meme(self,ctx):

		em = discord.Embed(title="Meme",description="Shows random meme from r/memes",color=discord.Color.green())
		em.add_field(name="**Syntax**", value="~meme")
		await ctx.send(embed=em)

	@help.command()
	async def kickinthenuts(self,ctx):

		em = discord.Embed(title="Kick in the nuts",description="Kicks specified player in the nuts",color=discord.Color.green())
		em.add_field(name="**Syntax**", value="~kickinthenuts <Target Player>")
		await ctx.send(embed=em)

	@help.command()
	async def play(self,ctx):

		em = discord.Embed(title="Play",description="Plays any youtube video of choice",color=discord.Color.green())
		em.add_field(name="**Syntax**", value="~play <yt_link>")
		await ctx.send(embed=em)

	@help.command()
	async def resume(self,ctx):

		em = discord.Embed(title="Resume",description="Resumes audio if paused",color=discord.Color.green())
		em.add_field(name="**Syntax**", value="~resume")
		await ctx.send(embed=em)

	@help.command()
	async def pause(self,ctx):

		em = discord.Embed(title="Pause",description="Pauses audio",color=discord.Color.green())
		em.add_field(name="**Syntax**", value="~pause")
		await ctx.send(embed=em)

	@help.command()
	async def stop(self,ctx):

		em = discord.Embed(title="Stop",description="Stops audio completely allowing you to play other songs/videos",color=discord.Color.green())
		em.add_field(name="**Syntax**", value="~stop")
		await ctx.send(embed=em)

	@help.command()
	async def leave(self,ctx):

		em = discord.Embed(title="leave",description="Leaves vc if connected to any",color=discord.Color.green())
		em.add_field(name="**Syntax**", value="~leave")
		await ctx.send(embed=em)

def setup(client):
	client.add_cog(Passive(client))