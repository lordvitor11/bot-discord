import os;
from random import choice;

interaction_ = None;
user_ = None

def run(interaction, user):
    global user_, interaction_
    pasta = "./otherfiles/kiss/";
    gifs = [];
    for diretorio, subpastas, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            if (arquivo != "kiss.gif"):
                gifs.append(os.path.join(diretorio, arquivo));

    if (interaction.user == user):
        return f"[ Erro ] {interaction.user.mention} Você não pode se beijar";
    else:
        if (user.bot):
            return f"[ Erro ] {interaction.user.mention} Bots não podem ser usados nesse comando"
        else:
            fileStr = choice(gifs)
            user_ = user
            interaction_ = interaction
            return [f"{interaction.user.mention} beijou {user.mention}", fileStr];



def retribute():
    pasta = "./otherfiles/kiss/";
    gifs = [];
    for diretorio, subpastas, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            if (arquivo == "kiss.gif"):
                gifs.append(os.path.join(diretorio, arquivo));

    return [f"{user_.mention} retribuiu o beijo de {interaction_.user.mention}", gifs[0], interaction_, user_];
    
    