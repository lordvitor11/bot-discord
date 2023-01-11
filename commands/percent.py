from random import randint;

def calc():
	porcent, porcent2 = randint(0, 10) * 10, randint(0, 10);
	porcent = str(porcent) + "%" if porcent == 100 else str(porcent + porcent2) + "%";

	return porcent;

def run(members, interaction, user, funct):
    commands = {0:"gay", 1:"hetero", 2:"nazista", 3:"fascista", 4:"crocante", 5:"gostoso", 6:"gostosa",
				7:"triste", 8:"feliz"};

    if user != None:
        if (not user.bot):
            if funct != 7:
                return f"{user.mention} é {calc()} {commands[funct]}"
            else:
                return f"{user.mention} está {calc()} {commands[funct]}"
        else:
            return f"Bots não podem ser usados neste comando!"
    else:
        if (funct != 7 and funct != 8):
            return f"{interaction.user.mention} é {calc()} {commands[funct]}"
        else:
            return f"{interaction.user.mention} está {calc()} {commands[funct]}"