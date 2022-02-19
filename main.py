import discord, asyncio
from discord.ext import commands
from defs import *
import token

intents = discord.Intents.default()
intents.members = True
intents.guilds = True

class Cleiton(commands.Bot):
	def __init__(self):
		super().__init__(command_prefix = ".", intents = intents, case_insensitive = True, help_command = None)

		#ADM COMMAND ZONE

		self.offruan = False

		#OFF
		@self.command(name = "off", description = "Desativa o bot(apenas ADM'S)")
		async def off(ctx):
			await ctx.channel.send(off_(ctx))
			quit()

		#MEMBER COMMAND ZONE

		#STATS
		@self.command(name = "stats", description = "Verifica se o bot está ativo")
		async def stats(ctx):
			await ctx.channel.send(stats_(ctx))

		#FATO
		@self.command(name = "fato", description = "Apresenta um fato aleatório")
		async def fato(ctx):
			await ctx.channel.send(fato_(ctx))

		#DADO
		@self.command(name = "dado", description = "Gera um número aleatório entre 1 e 6")
		async def dado(ctx):
			await ctx.channel.send(dado_(ctx))

		#GAY
		@self.command(name = "gay", description = "Fala uma porcentagem de gay")
		async def gay(ctx, arg = ""):
			await ctx.channel.send(porcent_commands(ctx, arg, 0))

		#HETERO
		@self.command(name = "hetero", description = "Fala uma porcentagem de hetero")
		async def hetero(ctx, arg = ""):
			await ctx.channel.send(porcent_commands(ctx, arg, 1))

		#NAZISTA
		@self.command(name = "nazista", description = "Fala uma porcentagem de nazista")
		async def nazista(ctx, arg = ""):
			await ctx.channel.send(porcent_commands(ctx, arg, 2))

		#FASCISTA
		@self.command(name = "fascista", description = "Fala uma porcentagem de fascista")
		async def fascista(ctx, arg = ""):
			await ctx.channel.send(porcent_commands(ctx, arg, 3))

		#CROCANTE
		@self.command(name = "crocante", description = "Fala uma porcentagem de crocancia")
		async def crocante(ctx, arg = ""):
			await ctx.channel.send(porcent_commands(ctx, arg, 4))

		#GOSTOSO
		@self.command(name = "gostoso", description = "Fala uma porcentagem de gostosura")
		async def gostoso(ctx, arg = ""):
			await ctx.channel.send(porcent_commands(ctx, arg, 5))

		#GOSTOSA
		@self.command(name = "gostosa", description = "Fala uma porcentagem de gostosura")
		async def gostosa(ctx, arg = ""):
			await ctx.channel.send(porcent_commands(ctx, arg, 6))

		#MONARK
		@self.command(name = "monark", description = "Fala uma porcentagem de nazista")
		async def monark(ctx, arg = ""):
			await ctx.channel.send(porcent_commands(ctx, arg, 2))

		#TRISTE
		@self.command(name = "triste", description = "retorna uma porcentagem de tristeza")
		async def triste(ctx, arg = ""):
			await ctx.channel.send(porcent_commands(ctx, arg, 7))

		#CHECKCUP
		@self.command(name = "checkup", description = "faz um checkup")
		async def checkup(ctx):
			await ctx.channel.send(embed = checkup_(ctx))

		#TAPA
		@self.command(name = "tapa", description = "Dá um tapa em alguém")
		async def tapa(ctx, arg = ""):
			await ctx.channel.send(tapa_(ctx, arg))

		#COBRAR
		@self.command(name = "cobrar", description = "Cobra alguém")
		async def tapa(ctx, arg = ""):
			await ctx.channel.send(cobrar_(ctx, arg))

		#ECHO
		@self.command(name = "echo", description = "Repete a frase digitada")
		async def echo(ctx, *arg):
			await ctx.channel.send(echo_(ctx, arg))

		#CASAL
		@self.command(name = "casal", description = "O bot monta casais")
		async def casal(ctx, arg = "", arg2 = ""):
			await ctx.channel.send(casal_amor(ctx, arg, arg2, self.get_guild(826202380818841641), 0))

		#AMOR
		@self.command(name = "amor", description = "Mostra a porcentagem de amor entre duas pessoas")
		async def amor(ctx, arg = "", arg2 = ""):
			await ctx.channel.send(casal_amor(ctx, arg, arg2, self.get_guild(826202380818841641), 1))

		#TOP10GADOS
		@self.command(name = "top10gados", description = "Mostra os 10 gados do servidor")
		async def top10gados(ctx):
			await ctx.channel.send(embed = top10(ctx, self.get_guild(826202380818841641), 0))

		#TOP10GOSTOSAS
		@self.command(name = "top10gostosas", description = "Mostra as 10 gostosas do servidor")
		async def top10gostosas(ctx):
			await ctx.channel.send(embed = top10(ctx, self.get_guild(826202380818841641), 1))

		#MOEDA
		@self.command(name = "moeda", description = "Retorna cara ou coroa")
		async def moeda(ctx):
			await ctx.channel.send(moeda_())

		#KISS
		@self.command(name = "kiss", description = "bejia alguem")
		async def kiss(ctx, arg = ""):	
			if "Erro" in kiss_hug(ctx, arg, 0):
				await ctx.channel.send(kiss_hug(ctx, arg, 0))
			else:
				await ctx.channel.send(kiss_hug(ctx, arg, 0), file=discord.File("./otherfiles/kiss.gif")) 	

		#BEIJAR
		@self.command(name = "beijar", description = "beija alguém")
		async def beijar(ctx, arg = ""):
			if "Erro" in kiss_hug(ctx, arg, 0):
				await ctx.channel.send(kiss_hug(ctx, arg, 0))
			else:
				await ctx.channel.send(kiss_hug(ctx, arg, 0), file=discord.File("./otherfiles/kiss.gif"))

		#HUG
		@self.command(name = "hug", description = "abraça alguém")
		async def hug(ctx, arg = ""):
			if "Erro" in kiss_hug(ctx, arg, 1):
				await ctx.channel.send(kiss_hug(ctx, arg, 1))
			else:
				await ctx.channel.send(kiss_hug(ctx, arg, 1), file=discord.File("./otherfiles/hug.gif"))	

		#ABRAÇAR
		@self.command(name = "abraçar", description = "abraça alguem")
		async def abraçar(ctx, arg = ""):
			if "Erro" in kiss_hug(ctx, arg, 1):
				await ctx.channel.send(kiss_hug(ctx, arg, 1))
			else:
				await ctx.channel.send(kiss_hug(ctx, arg, 1), file=discord.File("./otherfiles/hug.gif"))	
 
		#SUGGEST
		@self.command(name = "suggest", description = "Você pode sugerir uma inplementação se quiser")
		async def suggest(ctx):
			await ctx.reply(suggest_(ctx))

		#HELP
		@self.command(name = "help", description = "Mostra os comandos")
		async def help(ctx, arg = 1):
			if help_(ctx, arg) == "Página inexistente":
				await ctx.channel.send("Página inexistente", delete_after=4.5)
			else:
				await ctx.channel.send(ctx.author.mention, embed = help_(ctx, arg))

	async def on_ready(self):
		await self.change_presence(activity = discord.Game(name = ".help"))
		
	async def on_command_error(self, ctx, error):
		if isinstance(error, commands.CommandNotFound):
			embed = discord.Embed(title = "[ ERRO ]", description = f"Comando não encontrado. {ctx.author.mention} Digite .help para ver a lista de comandos!", color = ctx.author.color, delete_after=5.0)
			await ctx.channel.send(embed = embed)
	
	#MESSAGE FUNCS
	async def on_message(self, message):
		hora = datetime.now()
		fuso_horario = timezone("America/Sao_Paulo")
		hora = hora.astimezone(fuso_horario)
		hora = int(hora.strftime("%H"))

		if message.author == self.user:
			return

		if self.offruan == True:
			if message.author.id == 466726674013093897:
				await message.delete()

		if message.content.startswith("clbc ruan"):
			if message.author.id == subadm:
				self.offruan = True
				await message.reply(file=discord.File("./otherfiles/cleitofeliz.mp4"))

		if message.content.startswith("pode falar ruan"):
			if message.author.id == subadm:
				self.offruan = False

		if message.content.startswith("."):
			if ".ECHO" in message.content.upper():
				if message.channel.id != comandos:
					await self.process_commands(message)
					await message.delete()
			else:
				if message.channel.id != comandos:
					await self.process_commands(message)
		else:
			if message.channel.id != comandos:
				if message.content.upper().startswith("CONFIA"):
					await message.reply(file=discord.File("./otherfiles/confia.jpg"))

				if message.content.upper().startswith("SHALOM"):
					await message.reply(file=discord.File("./otherfiles/shalom.jpg"))

				if message.content.upper().startswith("NHAM NHAM"):
					await message.reply(file=discord.File("./otherfiles/nhamnham.gif"))	

				if message.content.upper().startswith("NOGUERA"):
					await message.reply(file=discord.File("./otherfiles/noguera.jpg"))

				if message.content.upper().startswith("PEDREIRO"):
					await message.reply(file=discord.File("./otherfiles/noguerasao.mp4"))

				if message.content.upper().startswith("REBOLA PRA MIM CLEITO"):
					await message.reply(file=discord.File("./otherfiles/cleitofeliz.mp4"))
					
				#if "@everyone Venham ver a live do patrão! https://www.twitch.tv/elkirito_" in message.content:
				#	await message.reply("<@!314051826288951307> vai amassar hoje, rs")	

				if message.content.upper().startswith("BOM DIA") or message.content.upper().startswith("BOA TARDE") or message.content.upper().startswith("BOA NOITE") or message.content.upper().startswith("BOA MADRUGADA"):
					a = message.content.split()
					a = f"{a[0].upper()} {a[1].upper()}"

					for hour in dayStats:
						if hora >= hour[1] and hora < hour[2]:
							if a == hour[0]:
								await message.reply(f"{a.capitalize()}! :)")
							else:
								await message.reply(f"Que {a.lower()} o que, zé, agora é {hour[0].split()[1].lower()}. A propósito, {hour[0].lower()}! :)")

			count = 0
			for c in range(len(prefixes)):
				if message.content.startswith(prefixes[c]):
					count += 1

			if count == 0:
				if not message.author.id in bots:
					if message.channel.id == comandos:
						await message.delete()

bot = Cleiton()
bot.run(open("token.txt", "r"))
