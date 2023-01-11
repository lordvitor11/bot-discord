from random import choice, randint;

def calc():
	porcent, porcent2 = randint(0, 10) * 10, randint(0, 10);
	porcent = str(porcent) + "%" if porcent == 100 else str(porcent + porcent2) + "%";

	return porcent;

def run(interaction, user, user2, funct):
    if (not user.bot and not user2.bot):
        if (user != user2):
            if (funct == 0):
                if (choice([0, 1]) == 0):
                    return f"{user.mention} e {user2.mention} formam um ótimo casal!"
                else:
                    return f"{user.mention} e {user2.mention} não formam um bom casal!"
            elif funct == 1:
                return f"O nível de amor entre {user.mention} e {user2.mention} é de {calc()}"
        else:
            return "Os usuários são iguais"
    else:
        return f"{interaction.user.mention} Bots não podem ser usados neste comando"
