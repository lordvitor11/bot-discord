from random import randint

def run(interaction):
    return f"{interaction.user.mention} Jogou o dado e tirou {randint(1, 6)}"