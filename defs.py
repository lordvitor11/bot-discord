import discord #pip install discord
from random import randint, choice
from datetime import datetime
from pytz import timezone

prefixes = ["!", "/", "-", "+", ".", "#", "$"]

#Memes escolhidos pela comunidade do discord
fatos =  ["Thiago é melhor que o nerd", "KITNET É RUIM", "Milena não tem sal", "O ADM é chato", "Carol é uma delicinha", 
		  "Ailton pedófilo", "Falta umildad no grupo", "Digite PEDREIRO e veja a mágica acontecer", "Carlin é depressivo",
		  "As Anas são tão presentes quanto pais de orfãos", "A mãe do Jorge é uma tremenda gostosa", "O ADM bebe leite puro", 
		  "Prima foi feita pra não comer a irmã", "ADM é o gadão guerreiro", "Thigazz se delecia da mãe de ruan", 'O grelo de "certas" pessoas tem 17 cm']

dayStats = [["BOM DIA", 6, 12], ["BOA TARDE", 12, 18], ["BOA NOITE", 18, 24], ["BOA MADRUGADA", 00, 6]]

bots = [547905866255433758, 297153970613387264, 235088799074484224, 282859044593598464, 882772337517285416]

adm, subadm, comandos, suggests = 438798320274767882, 314051826288951307, 826961049524895745, 883526463448576050

def calc():
	porcent, porcent2 = randint(0, 10) * 10, randint(0, 10)
	porcent = str(porcent) + "%" if porcent == 100 else str(porcent + porcent2) + "%"

	return porcent

def fato_(ctx):
	return fatos[randint(0, len(fatos) - 1)]

def dado_(ctx):
	return f"{ctx.author.mention} Jogou o dado e tirou {randint(1, 6)}"

#PORCENT COMMANDS
def porcent_commands(ctx, arg = "", funct = None):
	commands = {0:"gay", 1:"hetero", 2:"nazista", 3:"fascista", 4:"crocante", 5:"gostoso", 6:"gostosa",
				7:"triste"}

	if arg != "":
		if not int(arg.replace("<@!>")) in bots:
			if funct != 7:
				return f"{arg} é {calc()} {commands[funct]}"
			else:
				return f"{arg} está {calc()} {commands[funct]}"
		else:
			return f"Bots não podem ser usados neste comando!"
	else:
		if funct != 7:
			return f"{ctx.author.mention} é {calc()} {commands[funct]}"
		else:
			return f"{ctx.author.mention} está {calc()} {commands[funct]}"

def tapa_(ctx, arg):
	if arg == "":
		return f"{ctx.author.mention} ficou maluco(a) e estapeou-se"
	else:
		return f"{ctx.author.mention} estapeou {arg}"

def cobrar_(ctx, arg):
	if arg == "":
		return f"{ctx.author.mention} Comando utilizado de maneira errada!\nUtilização: .cobrar @usuário"
	else:
		return f"{ctx.author.mention} Pode deixar, vou cobrar..."

def echo_(ctx, arg, arg2 = ""):
	if len(arg) > 0:
		for c in range(len(arg)):
			arg2 += f"{arg[c]} "

		arg2 = arg2.strip()
		return arg2

def casal_amor(ctx, arg, arg2, guild, funct):
	if arg != "" and arg2 != "":
		if int("".join(x for x in arg if x not in "<@!>")) in bots or int("".join(x for x in arg2 if x not in "<@!>")) in bots:
			return f"{ctx.author.mention} Bots não podem ser usados neste comando"
		elif arg != "" and arg2 != "":
			if arg != arg2:
				if funct == 0:
					return f"{arg} e {arg2} formam um ótimo casal!"
				elif funct == 1:
					return f"O nível de amor entre {arg} e {arg2} é de {calc()}"
		elif arg != "" and arg2 == "":
			if arg != f"<@!{ctx.author.id}>":
				if funct == 0:
					return f"{ctx.author.mention} e {arg} formam um ótimo casal!"
				elif funct == 1:
					return f"O nível de amor entre {ctx.author.mention} e {arg} é de {calc()}"
	else:
		members = []

		for member in guild.members:
			if not member.id in bots:
				members.append(str(member.id))

		while True:
			escolhido = choice(members)
			if ctx.author.id != escolhido:
				if funct == 0:
					return f"{ctx.author.mention} e <@!{escolhido}> formam um ótimo casal!"
				elif funct == 1:
					return f"O nível de amor entre {ctx.author.mention} e <@!{escolhido}> é de {calc()}"

def top10(ctx, guild, funct):
	members, filtred = [], []
	a = "gados" if funct == 0 else "gostosas"
	embed = discord.Embed(title = f"Top 10 {a} do servidor:", description = "", colour = 11598249)

	for member in guild.members:
		if not member.name in ["Loritta", "Hydra", "ProBot ✨", "Rythm", "Cleiton, o portador da verdade"]:
			members.append(str(member.name))

	while True:
		escolhido = choice(members)
		if not escolhido in filtred:
			filtred.append(escolhido)

		if len(filtred) == 10:
			break

	for c in range(len(filtred)):
		embed.add_field(name = f"#{c + 1} {filtred[c]}", value = "⠀", inline = False)

	return embed

def moeda_():
	if randint(0, 1) == 0:
		return "Cara :slightly_frowning_face:"
	else:
		return "Coroa :crown:"

def suggest_(ctx):
	return f"Você pode sugerir funções em <#{suggests}>"

def checkup_(ctx):
	embed = discord.Embed(title = "Checkup Stats", description = ctx.author.mention, color = ctx.author.color)
	gay, hetero = int(calc().replace("%", "")), int(calc().replace("%", ""))
	crocante, gostoso = int(calc().replace("%", "")), int(calc().replace("%", ""))

	if gay > hetero:
		hetero = 100 - gay
	else:
		gay = 100 - hetero

	if crocante > gostoso:
		gostoso = 100 - crocante
	else:
		crocante = 100 - gostoso

	embed.add_field(name = f"Gay: {gay}%", value = "⠀", inline = False)
	embed.add_field(name = f"Hétero: {hetero}%", value = "⠀", inline = False)
	embed.add_field(name = f"Nazista: {calc()}", value = "⠀", inline = False)
	embed.add_field(name = f"Fascista: {calc()}", value = "⠀", inline = False)
	embed.add_field(name = f"Crocante: {crocante}%", value = "⠀", inline = False)
	embed.add_field(name = f"Gostoso(a): {gostoso}%", value = "⠀", inline = False)
	embed.add_field(name = f"Triste: {calc()}", value = "⠀", inline = False)

	return embed

def kiss_hug(ctx, arg, funct):
	if arg == "":
		return f"[ Erro ] {ctx.author.mention} Você deve mencionar alguém nesse comando"

	NArg = int("".join(x for x in arg if x not in "<!@>"))

	if ctx.author.id == NArg:
		if funct == 0:
			return f"[ Erro ] {ctx.author.mention} Você não pode se beijar"
		else:
			return f"[ Erro ] {ctx.author.mention} Você não pode se abraçar"
	elif NArg in bots:
		return f"[ Erro ] {ctx.author.mention} Bots não podem ser usados nesse comando"
	else:
		if funct == 0:
			return f"{ctx.author.mention} beijou {arg}"
		else:
			return f"{ctx.author.mention} abraçou {arg}"
		
def help_(ctx, arg):
	embed = discord.Embed(title = "Comandos:", description = "Prefixo: .", color = ctx.author.color)

	if arg == 1:
		embed.add_field(name = "Stats", value = "Verifica se o bot está funcionando", inline = False)
		embed.add_field(name = "Fato", value = "Apresenta um fato aleatório", inline = False)
		embed.add_field(name = "Dado", value = "Joga um dado", inline = False)
		embed.add_field(name = "Suggest", value = "Você pode sugerir uma mudança em mim :)", inline = False)
		embed.add_field(name = "Gay", value = "Veja o quão gay é uma pessoa(utilização: .gay ou .gay @usuário)", inline = False)
		embed.add_field(name = "Hetero", value = "Veja o quão hétero é uma pessoa(utilização: .hetero ou .hetero @usuário)", inline = False)
		embed.add_field(name = "Nazista ou Monark", value = "Veja o quão nazista é uma pessoa(utilização: .nazista ou .nazista @usuário)", inline = False)
		embed.add_field(name = "Fascista", value = "Veja o quão fascista é uma pessoa(utilização: .fascista ou .fascismo @usuário)", inline = False)
		embed.add_field(name = "Casal", value = "O bot forma um casal(utilização: .casal(procura uma pessoa aleatória) ou .casal @usuário ou .casal @usuário @usuário2)", inline = False)
		embed.add_field(name = "Pág. 1 de 3", value = "Use: .help [numerodapagina] para ver outras páginas", inline = False)
	elif arg == 2:
		embed.add_field(name = "Amor", value = "Veja as chances que você tem com tal pessoa(utilização: .amor(procura uma pessoa aleatória) ou .amor @usuário ou .amor @usuário @usuário2)", inline = False)
		embed.add_field(name = "Tapa", value = "Dê um tapa em alguém(utilização: .tapa ou .tapa @usuário)", inline = False)
		embed.add_field(name = "Cobrar", value = "O bot cobra alguém(utilização: .cobrar @usuário)", inline = False)
		embed.add_field(name = "Top10gados", value = "Mostra o top 10 gados do servidor", inline = False)
		embed.add_field(name = "Top10gostosas", value = "Mostra o top 10 gostosas do servidor", inline = False)
		embed.add_field(name = "Echo", value = "Repete a frase digitada(utilização: .echo [ frase ])", inline = False)
		embed.add_field(name = "Moeda", value = "Retorna cara ou coroa", inline = False)
		embed.add_field(name = "Crocante", value = "Veja o quão crocante é uma pessoa(utilização: .crocante ou .crocante @usuário)", inline = False)
		embed.add_field(name = "Gostoso", value = "Veja o quão gostoso(a) é uma pessoa(utilização: .gostoso ou .gostoso @usuário)", inline = False)
		embed.add_field(name = "Pág. 2 de 3", value = "Use: .help [numerodapagina] para ver outras páginas", inline = False)
	elif arg == 3:
		embed.add_field(name = "Kiss ou Beijar", value = "Beija alguém. Utilização: .kiss/.beijar @usuário", inline = False)
		embed.add_field(name = "Hug ou Abraçar", value = "Abraça alguém. Utilização: .hug/.abraçar @usuário", inline = False)

		embed.add_field(name = "Pág. 3 de 3", value = "Use: .help [numerodapagina] para ver outras páginas", inline = False)
	else:
		return "Página inexistente"

	embed.set_footer(text = "Version: 0.4.3a")
	return embed
