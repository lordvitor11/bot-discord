import discord;
from random import choice;

def run(guild, funct):
	members, filtred = [], [];
	a = "gados" if funct == 0 else "gostosos(as)";
	embed = discord.Embed(title = f"Top 10 {a} do servidor:", description = "", colour = 11598249);

	for member in guild.members:
		if (not member.bot):
			members.append(str(member.name));

	while True:
		escolhido = choice(members);
		if (not escolhido in filtred):
			filtred.append(escolhido);

		if len(filtred) == 10:
			break;

	for c in range(len(filtred)):
		embed.add_field(name = f"#{c + 1} {filtred[c]}", value = "⠀", inline = False);

	return embed;
