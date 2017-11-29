import discord
from discord.ext import commands

class Rules:
	def __init__(self,bot):
		self.bot = bot

	def rulesEmbed(self, rulenumber, ruledescription):
		'''Function to quickly generate a rule'''
		footer_icon = 'https://images-ext-1.discordapp.net/external/_PkFdSwUn0fEDz8-FjOd9AGKcLAkCKOALCaR--l8twI/https/cdn.discordapp.com/emojis/349312608387596299.png'
		embed = discord.Embed(title="Rule " + rulenumber, description=ruledescription)
		embed.set_footer(text="This embed is part of Pedro. © Ev1l0rd, 2017, GPLv3", icon_url=footer_icon)
		return embed

	# Rule 1
	@commands.command()
	async def r1(self,ctx):
		'''Output rule 1'''
		rule1 = self.rulesEmbed("1","Don't be a jerk. Be kind to other people and help them out.\n  - This rule is also talking about messing with Paul because of the unbanmii situation")
		await ctx.send(embed=rule1)

	# Rule 2
	@commands.command()
	async def r2(self,ctx):
		'''Output rule 2'''
		rule2 = self.rulesEmbed("2","No piracy. Don't link to warez - this includes the key site, the angel tool and any other tools that permit direct downloading from Nintendo's CDN.\n- We reserve the right to deny support to anyone suspected of using the tool for piracy.")
		await ctx.send(embed=rule2)

	@commands.command()
	async def r3(self,ctx):
		'''Output rule 3'''
		rule3 = self.rulesEmbed("3",'No alts, at least without asking a moderator first.\n- In order to get activated, you\'ll need to say "bonedirector" in #approval and write a short approval message describing how you found this discord. Try and work the word in this message as naturally as possible.')
		await ctx.send(embed=rule3)

	@commands.command()
	async def r4(self,ctx):
		'''Output rule 4'''
		rule4 = self.rulesEmbed("4","Don't spam. This falls under rule 1 but I want to be explicit.")
		await ctx.send(embed=rule4)

	@commands.command()
	async def r5(self,ctx):
		'''Output rule 5'''
		rule5 = self.rulesEmbed("5",'Don\'t bring up drama. This falls under rule 1 but I want to be explicit.\n  - This includes importing drama from other servers. Hash it out there or in DMs. \n  - This rule also prohibits questions like "will freeshop contain malware?"(freeShop is open source: If you don\'t trust the code, you can always check it yourself and compile it.)')
		await ctx.send(embed=rule5)

	@commands.command()
	async def r6(self,ctx):
		'''Output rule 6'''
		rule6 = self.rulesEmbed("6","NSFW is prohibited")
		await ctx.send(embed=rule6)

	@commands.command()
	async def r7(self,ctx):
		'''Output rule 7'''
		rule7 = self.rulesEmbed("7","Don't ask for any roles")
		await ctx.send(embed=rule7)

	@commands.command()
	async def r8(self,ctx):
		'''Output rule 8'''
		rule8 = self.rulesEmbed("8","The cache updates on Monday, Wednesday & Saturday. Don't ask if it has updated, or for an update. The cache maintainer has a life outside of Freeshop.")
		await ctx.send(embed=rule8)

	@commands.command()
	async def r9(self,ctx):
		'''Output rule 9'''
		rule9 = self.rulesEmbed("9","All decisions by staff are final and not up to public debate. If you have a concern, take it up privately or in #meta.")
		await ctx.send(embed=rule9)

	@commands.command()
	async def r10(self,ctx):
		'''Output rule 10'''
		rule10 = self.rulesEmbed("10","No slurs.")
		await ctx.send(embed=rule10)

class freeShopMisc:
	def __init__(self,bot):
		self.bot = bot

	@commands.command()
	async def qr(self,ctx):
		'''Shows a QR code for the latest version of freeShop'''
		footer_icon = 'https://images-ext-1.discordapp.net/external/_PkFdSwUn0fEDz8-FjOd9AGKcLAkCKOALCaR--l8twI/https/cdn.discordapp.com/emojis/349312608387596299.png'
		qr = discord.Embed(title="freeShop QR code")
		qr.set_image(url='https://gbatemp.net/attachments/qr-code-2-png.97734')
		qr.set_footer(text="This embed is part of Pedro. © Ev1l0rd, 2017, GPLv3", icon_url=footer_icon)
		await ctx.send(embed=qr)

def setup(bot):
	bot.add_cog(Rules(bot))
	print('Loaded rules cog...')
	bot.add_cog(freeShopMisc(bot))
	print('Loaded freeShopMisc cog...')