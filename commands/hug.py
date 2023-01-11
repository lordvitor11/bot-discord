import os;
from random import choice;

interaction_ = None;
user_ = None

def run(interaction, user):
    global user_, interaction_
    pasta = "./otherfiles/hug/";
    gifs = [];
    for diretorio, subpastas, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            if (arquivo != "hug.gif"):
                gifs.append(os.path.join(diretorio, arquivo));

    if (interaction.user == user):
        return f"[ Erro ] {interaction.user.mention} Você não pode se abraçar";
    else:
        if (user.bot):
            return f"[ Erro ] {interaction.user.mention} Bots não podem ser usados nesse comando"
        else:
            fileStr = choice(gifs)
            user_ = user
            interaction_ = interaction
            return [f"{interaction.user.mention} abraçou {user.mention}", fileStr];



def retribute():
    pasta = "./otherfiles/hug/";
    gifs = [];
    for diretorio, subpastas, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            if (arquivo == "hug.gif"):
                gifs.append(os.path.join(diretorio, arquivo));

    return [f"{user_.mention} retribuiu o abraço de {interaction_.user.mention}", gifs[0], interaction_, user_];
    
    