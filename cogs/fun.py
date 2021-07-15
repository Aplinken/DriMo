import discord
import requests
import random
from discord.ext import commands
from PIL import Image
from io import BytesIO



class Fun(commands.Cog):
	def __init__(self,client):
		self.client = client


	@commands.command()
	async def meme(self,ctx):
		with open('personal.txt') as f:
			personal = f.read()
		with open('secret.txt') as f:
			secret = f.read()
		auth = requests.auth.HTTPBasicAuth(personal, secret)
		with open('pass.txt') as f:
			password = f.read()
		data = {'grant_type' : 'password',
				'username' : 'Aplinken',
				'password' : password}

		headers = {'User-Agent': 'newbings/0.0.1'}
		res = requests.post('https://www.reddit.com/api/v1/access_token', auth = auth, data = data, headers = headers)
		token = res.json()["access_token"]

		headers['Authorization'] = f'bearer {token}'
		res = requests.get('https://oauth.reddit.com/r/memes/random', headers=headers)
		random_post = res.json()[0]['data']['children'][0]['data']

		em = discord.Embed(title = random_post['title'])
		em.set_image(url = random_post['url'])

		await ctx.send(embed=em)

	@commands.command(aliases=['8ball'])
	async def _8ball(self,ctx):
		all_responses=['It is certain','Without a doubt','My reply is no','Concentrate and ask again',
		'As i see it, yes','My sources say no','Outlook not so good','Yes - Definitely','Most likely']

		random_response = random.choice(all_responses)
		await ctx.send(random_response)

	@commands.command()
	async def kickinthenuts(self,ctx,user: discord.Member = None):
		if user == None:
			await ctx.send("Mention a user that you want to kick dummy!")
		else:
			kick = Image.open("kickinthenuts.jpg")

			asset_one = ctx.author.avatar_url_as(size=64)
			asset_two = user.avatar_url_as(size=64)
			data_one = BytesIO(await asset_one.read())
			data_two = BytesIO(await asset_two.read())
			pfp_one = Image.open(data_one)
			pfp_two = Image.open(data_two)

			pfp_one.resize((59,59))
			pfp_two.resize((56,55))

			kick.paste(pfp_one, (31,3))
			kick.paste(pfp_two, (205,8))
			kick.save("kickdone.jpg")

			await ctx.send(file=discord.File("kickdone.jpg"))

def setup(client):
	client.add_cog(Fun(client))