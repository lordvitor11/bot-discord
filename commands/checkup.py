import discord
from random import randint;

def calc():
	porcent, porcent2 = randint(0, 10) * 10, randint(0, 10);
	porcent = str(porcent) + "%" if porcent == 100 else str(porcent + porcent2) + "%";

	return porcent;

def run(interaction):
    embed = discord.Embed(title = "Checkup Stats", description = interaction.user.mention, color = interaction.user.color)
    gay, hetero = int(calc().replace("%", "")), int(calc().replace("%", ""))
    crocante, gostoso = int(calc().replace("%", "")), int(calc().replace("%", ""))
    feliz, triste = int(calc().replace("%", "")), int(calc().replace("%", ""))

    print(feliz, triste)

    if (gay > hetero): hetero = 100 - gay
    else: gay = 100 - hetero

    if (crocante > gostoso): gostoso = 100 - crocante;
    else: crocante = 100 - gostoso;

    if (triste > feliz): feliz = 100 - triste;
    else: triste = 100 - feliz;

    embed.add_field(name = f"Gay:", value = f"{gay}%⠀", inline = True);
    embed.add_field(name = f"Hétero:", value = f"{hetero}%⠀", inline = True);
    embed.add_field(name = f"Nazista:", value = f"{calc()}⠀", inline = True);
    embed.add_field(name = f"Fascista:", value = f"{calc()}⠀", inline = True);
    embed.add_field(name = f"Crocante:", value = f"{crocante}%⠀", inline = True);
    embed.add_field(name = f"Gostoso(a):", value = f"{gostoso}%⠀", inline = True);
    embed.add_field(name = f"Triste:", value = f"{triste}%⠀", inline = True);
    embed.add_field(name = f"Feliz:", value = f"{feliz}%⠀", inline = True);
    embed.set_thumbnail(url = interaction.user.avatar)

    return embed;
