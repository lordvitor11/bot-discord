# pip intall discord.py pytz

import discord, asyncio;
from discord import app_commands;
from commands import fact, dice, percent, checkup, cupid, top10, kiss, hug, slap;
from random import randint;
from datetime import datetime;
from pytz import timezone;


intents = discord.Intents.all();
guildId = 826202380818841641;
guild = discord.Object(id = guildId);
comandos = 826961049524895745;

class Main(discord.Client):
    def __init__(self):
        super().__init__(intents=intents);
        self.synced = False;

    async def on_ready(self):
        await self.wait_until_ready();
        if not self.synced:
            await tree.sync(guild = guild);
            self.synced = True;

        print(f"Logado como {self.user}");

    async def on_message(self, interaction):
        hora = datetime.now()
        fuso_horario = timezone("America/Sao_Paulo")
        hora = hora.astimezone(fuso_horario)
        hora = int(hora.strftime("%H"))
        cmds = ["BOA MADRUGADA", "BOM DIA", "BOA TARDE", "BOA NOITE"]
        filesCmd = [ "CONFIA", "NOGUERA", "PEDREIRO", "REBOLA CLEITO", "REBOLA PRA MIM CLEITO"]
        dayStats = [["BOM DIA", 6, 12], ["BOA TARDE", 12, 18], ["BOA NOITE", 18, 24], ["BOA MADRUGADA", 00, 6]]

        if (interaction.author) == self.user: return

        if (not interaction.author.bot):
            if (interaction.channel.id == comandos):
                await interaction.delete()

        if (interaction.channel.id != comandos):
            check = interaction.content.upper();
            for item in filesCmd: 
                if (check.startswith(item)): check = item;

            match (check):
                case "CONFIA":
                    await interaction.reply(file=discord.File("./otherfiles/confia.jpg"));
                case "NOGUERA":
                    await interaction.reply(file=discord.File("./otherfiles/noguera.jpg"))
                case "PEDREIRO":
                    await interaction.reply(file=discord.File("./otherfiles/noguerasao.mp4"))
                case "REBOLA PRA MIM CLEITO":
                    await interaction.reply(file=discord.File("./otherfiles/cleitofeliz.mp4"))
                case "REBOLA CLEITO":
                    await interaction.reply(file=discord.File("./otherfiles/cleitofeliz.mp4"))
                case _: pass;


            check = interaction.content.upper();
            for item in cmds: 
                if (check.startswith(item)): check = item;

            if (check in cmds):
                a = interaction.content.split()
                a = f"{a[0].upper()} {a[1].upper()}"
                a = "".join(e for e in a if e.isalpha() or e.isspace())

                for hour in dayStats:
                    if hora >= hour[1] and hora < hour[2]:
                        if a == hour[0]:
                            await interaction.reply(f"{a.capitalize()}! :)")
                        else:
                            await interaction.reply(f"Que {a.lower()} o que, zé, agora é {hour[0].split()[1].lower()}. A propósito, {hour[0].lower()}! :)")

class SlapButton(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)

    @discord.ui.button(label = "Retribuir", style = discord.ButtonStyle.blurple)
    async def retribute(self, interaction: discord.Interaction, button: discord.ui.Button):
        response = slap.retribute();

        if (response[3] == interaction.user):
            embed = discord.Embed(description = response[0], color = interaction.user.color);
            file = discord.File(response[1], filename="image.gif")
            embed.set_image(url="attachment://image.gif")

            await interaction.response.defer();
            await asyncio.sleep(1);
            await interaction.followup.send(file = file, embed = embed);
        else:
            button.style = discord.ButtonStyle.red

class HugButton(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)

    @discord.ui.button(label = "Retribuir", style = discord.ButtonStyle.blurple)
    async def retribute(self, interaction: discord.Interaction, button: discord.ui.Button):
        response = hug.retribute();

        if (response[3] == interaction.user):
            embed = discord.Embed(description = response[0], color = interaction.user.color);
            file = discord.File(response[1], filename="image.gif")
            embed.set_image(url="attachment://image.gif")

            await interaction.response.defer();
            await asyncio.sleep(1);
            await interaction.followup.send(file = file, embed = embed);
        else:
            button.style = discord.ButtonStyle.red

class KissButton(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)

    @discord.ui.button(label = "Retribuir", style = discord.ButtonStyle.blurple)
    async def retribute(self, interaction: discord.Interaction, button: discord.ui.Button):
        response = kiss.retribute();

        if (response[3] == interaction.user):
            embed = discord.Embed(description = response[0], color = interaction.user.color);
            file = discord.File(response[1], filename="image.gif")
            embed.set_image(url="attachment://image.gif")

            await interaction.response.defer();
            await asyncio.sleep(1);
            await interaction.followup.send(file = file, embed = embed);
        else:
            button.style = discord.ButtonStyle.red

bot = Main();
tree = app_commands.CommandTree(bot);


@tree.command(name = "fato", description = "Apresenta um fato aleatório", guild = guild)
async def self(interaction: discord.Interaction):
    await interaction.response.send_message(fact.run());

@tree.command(name = "dado", description = "Gera um número aleatório entre 1 e 6", guild = guild)
async def self(interaction: discord.Interaction):
    await interaction.response.send_message(dice.run(interaction)); 

@tree.command(name = "gay", description = "Retorna uma porcentagem de gay", guild = guild)
async def self(interaction: discord.Interaction, usuario: discord.User = None):
    await interaction.response.send_message(percent.run(interaction.guild.members, interaction, usuario, 0));

@tree.command(name = "hetero", description = "Retorna uma porcentagem de hétero", guild = guild)
async def self(interaction: discord.Interaction, usuario: discord.User = None):
    await interaction.response.send_message(percent.run(interaction.guild.members, interaction, usuario, 1));

@tree.command(name = "nazista", description = "Retorna uma porcentagem de nazista", guild = guild)
async def self(interaction: discord.Interaction, usuario: discord.User = None):
    await interaction.response.send_message(percent.run(interaction.guild.members, interaction, usuario, 2));

@tree.command(name = "fascista", description = "Retorna uma porcentagem de fascista", guild = guild)
async def self(interaction: discord.Interaction, usuario: discord.User = None):
    await interaction.response.send_message(percent.run(interaction.guild.members, interaction, usuario, 3));

@tree.command(name = "crocante", description = "Retorna uma porcentagem de crocante", guild = guild)
async def self(interaction: discord.Interaction, usuario: discord.User = None):
    await interaction.response.send_message(percent.run(interaction.guild.members, interaction, usuario, 4));

@tree.command(name = "gostoso", description = "Retorna uma porcentagem de gostosura", guild = guild)
async def self(interaction: discord.Interaction, usuario: discord.User = None):
    await interaction.response.send_message(percent.run(interaction.guild.members, interaction, usuario, 5));

@tree.command(name = "gostosa", description = "Retorna uma porcentagem de gostosura", guild = guild)
async def self(interaction: discord.Interaction, usuario: discord.User = None):
    await interaction.response.send_message(percent.run(interaction.guild.members, interaction, usuario, 6));

@tree.command(name = "triste", description = "Retorna uma porcentagem de tristeza", guild = guild)
async def self(interaction: discord.Interaction, usuario: discord.User = None):
    await interaction.response.send_message(percent.run(interaction.guild.members, interaction, usuario, 7));

@tree.command(name = "feliz", description = "Retorna uma porcentagem de felicidade", guild = guild)
async def self(interaction: discord.Interaction, usuario: discord.User = None):
    await interaction.response.send_message(percent.run(interaction.guild.members, interaction, usuario, 8));

@tree.command(name = "checkup", description = "Faz um checkup", guild = guild)
async def self(interaction: discord.Interaction):
    await interaction.response.send_message(embed = checkup.run(interaction));

@tree.command(name = "cobrar", description = "Cobra um usuário", guild = guild)
async def self(interaction: discord.Interaction):
    await interaction.response.send_message(f"{interaction.user.mention} Pode deixar, vou cobrar...");

@tree.command(name = "echo", description = "Retorna a mensagem passada", guild = guild)
async def self(interaction: discord.Interaction, mensagem: str):
    await interaction.response.send_message(mensagem);

@tree.command(name = "moeda", description = "Retorna cara ou coroa")
async def self(interaction: discord.Interaction):
    await interaction.response.send_message("Cara :slightly_frowning_face:" if randint(0, 1) == 0 else "Coroa :crown:");

@tree.command(name = "casal", description = "O Cleito vira um cúpido", guild = guild)
async def self(interaction: discord.Interaction, usuario: discord.User, usuario2: discord.User):
    await interaction.response.send_message(cupid.run(interaction, usuario, usuario2, 0));

@tree.command(name = "amor", description = "O Cleito vira um cúpido", guild = guild)
async def self(interaction: discord.Interaction, usuario: discord.User, usuario2: discord.User):
    await interaction.response.send_message(cupid.run(interaction, usuario, usuario2, 1));

@tree.command(name = "top10gados", description = "Mostra os 10 mais gados do server", guild = guild)
async def self(interaction: discord.Interaction):
    await interaction.response.send_message(embed = top10.run(interaction.guild, 0));

@tree.command(name = "top10gostosas", description = "Mostra os(as) 10 mais gostosos(as) do server", guild = guild)
async def self(interaction: discord.Interaction):
    await interaction.response.send_message(embed = top10.run(interaction.guild, 1));

@tree.command(name = "tapa", description = "Bate em um usuário", guild = guild)
async def self(interaction: discord.Interaction, usuario: discord.User):
    if "Erro" in slap.run(interaction, usuario):
        await interaction.response.send_message(slap.run(interaction, usuario));
    else:
        response = slap.run(interaction, usuario);
        embed = discord.Embed(description = response[0], color = interaction.user.color);
        file = discord.File(response[1], filename="image.gif")
        embed.set_image(url="attachment://image.gif")


        await interaction.response.send_message(file = file, embed = embed, view = SlapButton());

@tree.command(name = "hug", description = "Abraça um usuário", guild = guild)
async def self(interaction: discord.Interaction, usuario: discord.User):
    if "Erro" in hug.run(interaction, usuario):
        await interaction.response.send_message(hug.run(interaction, usuario));
    else:
        response = hug.run(interaction, usuario);
        embed = discord.Embed(description = response[0], color = interaction.user.color);
        file = discord.File(response[1], filename="image.gif")
        embed.set_image(url="attachment://image.gif")


        await interaction.response.send_message(file = file, embed = embed, view = HugButton());

@tree.command(name = "kiss", description = "Abraça um usuário", guild = guild)
async def self(interaction: discord.Interaction, usuario: discord.User):
    if "Erro" in kiss.run(interaction, usuario):
        await interaction.response.send_message(kiss.run(interaction, usuario));
    else:
        response = kiss.run(interaction, usuario);
        embed = discord.Embed(description = response[0], color = interaction.user.color);
        file = discord.File(response[1], filename="image.gif")
        embed.set_image(url="attachment://image.gif")


        await interaction.response.send_message(file = file, embed = embed, view = KissButton());

bot.run(open("token.txt", "r").read()) #Pegar o token do bot através de um arquivo de texto
