# This is a sample Python script.
import asyncio
from JRole import JRole
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
import random
from discord.ext.commands import Bot

Liste2 = []
ListeJoueur = []
bot = commands.Bot(command_prefix="!", description="Bot ToS", intents=intents)
verif = False
PasserTour=False
Nb_Roles = 30
Nb_Perso_Co = 7

roles = ['Garde du Corps', 'Maire', 'Medecin', 'Escorte', 'Parrain', 'Epouse', 'Mafieux', 'Amnésique', 'Enqueteur',
         'Geolier', 'Consigliere', 'Pyromane', 'Chercheur', 'Voyant', 'Deguisement', 'Faussaire', 'Bourreau',
         'Retribution', 'Sherif', 'Encadreur', 'Ange Gardien', 'Espion', 'Transporteur', 'Concierge', 'Hypnotiseur',
         'Bouffon', 'Chasseur de Vampire', 'Veteran', 'Embuscade', 'Mastodonte', 'Vigilant', 'Croisés', 'Pirate',
         'Porte Peste', 'Traqueur', 'Trappeur', 'Tueur en série', 'Survivant', 'Vampire', 'Loup Garou', 'Sorciere',
         'Psychique']
taken_roles = []


@bot.event
async def on_ready():
    print("a")


@bot.command()
async def Jouer(ctx):
    global verif
    verif = True

def CheckNom(f):
    nam = ""
    for Jo in Liste2:
        print(Jo.Role)
        if Jo.Role == f:
            nam = Jo.getnom()
    return nam

def verif_list(list, position):
    return position in list

@bot.command()
async def commence(ctx):
    print(len(ctx.guild.members))
    global verif
    await ctx.send("le jeu va commencer")
    message = await ctx.send("Commencez par définir les joueurs de la partie", delete_after=35)
    reactions = ['✅']
    for emoji in reactions:
        await message.add_reaction(emoji)
        break
    Joueur = await ctx.guild.create_role(name="Joueur")


    # Inscription
    p = 0
    print(verif)
    while p < 14 and verif != True:
        reaction, member = await bot.wait_for("reaction_add")
        if reaction.emoji == '✅':
            var = discord.utils.get(message.guild.roles, name="Joueur")
            await member.add_roles(var)
            #   RETIRER LE GRADE A LA FIN DE LA PARTIE
            ListeJoueur.append(member.display_name)
            x = ctx.guild.get_member_named(ListeJoueur[p])
            print(x)
            print(p)
            print(ListeJoueur)
            print(Liste2)
            p += 1
            print(verif)

        #Attribution des roles
        for i in range(len(ListeJoueur)):
            random_roles = random.randint(0, Nb_Perso_Co+1)
            mon_role_aleatoire = roles[random_roles]
            if not verif_list(taken_roles, random_roles):
                print("Membre numéro ", i, " : ", mon_role_aleatoire)
                Liste2.append(JRole(mon_role_aleatoire, x))
                taken_roles.append(random_roles)
            else:
                while verif_list(taken_roles, random_roles):
                    random_roles = random.randint(0, Nb_Perso_Co)
                    mon_role_aleatoire = roles[random_roles]
                Liste2.append(JRole(mon_role_aleatoire, x))
                taken_roles.append(random_roles)
                print("Membre numéro ", i, " : ", mon_role_aleatoire)


    autorize = ctx.guild.get_role(Joueur.id)
    overwrites = {
        ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
        ctx.guild.me: discord.PermissionOverwrite(read_messages=True),
        autorize: discord.PermissionOverwrite(read_messages=True)
    }
    channel = await ctx.guild.create_text_channel('General', overwrites=overwrites)
    await ctx.send("La nuit peut commencer")

    #Escorte
    await ctx.send("L'escorte se reveille")

    E = CheckNom("Escorte")
    while E!="":
        overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            ctx.guild.me: discord.PermissionOverwrite(read_messages=True),
            E: discord.PermissionOverwrite(read_messages=True)
        }

        channelE = await ctx.guild.create_text_channel('Escorte', overwrites=overwrites)
        cE = bot.get_channel(channelE.id)
        await cE.send("Ecrivez le nom de la personne que vous voulez distraire par exemple:Toto Titi#1234")
        verif1 = False

        while verif1 == False:
            print("aaaa")

            def check(m):
                return m.channel == cE

            msg = await bot.wait_for("message", check=check)
            var = (msg.content)
            cible = ctx.guild.get_member_named(var)

            if cible != None:
                verif1 = True
                for Jo in Liste2:
                    print(2)
                if Jo.nom == cible:
                    if Jo.Role != "Epouse":
                        Jo.Distraire()
                        print(Jo.Distract)
            if verif1 == False:
                await cE.send("Il faut que vous recommenciez")
        await cE.send("C'est bon")
        E=""
    await ctx.send("L'escorte se rendort")
    #Epouse
    await ctx.send("L'epouse se reveille")
    Ep = CheckNom("Epouse")
    while Ep != "":
        overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            ctx.guild.me: discord.PermissionOverwrite(read_messages=True),
            Ep: discord.PermissionOverwrite(read_messages=True)
        }

        channelEp = await ctx.guild.create_text_channel('Epouse', overwrites=overwrites)
        cEp = bot.get_channel(channelEp.id)
        await cEp.send("Ecrivez le nom de la personne que vous voulez distraire par exemple:Toto Titi#1234")
        verif4 = False

        while verif4 == False:
            print("aaaa")

            def check(m):
                return m.channel == cEp

            msg = await bot.wait_for("message", check=check)
            var = (msg.content)
            cible = ctx.guild.get_member_named(var)

            if cible != None:
                for Jo in Liste2:
                    print(2)
                    if Jo.nom == cible:
                        verif4 = True
                        if Jo.Role != "Escorte":
                            Jo.Distraire()
                            print(Jo.Distract)
            if verif4 == False:
                await cEp.send("Il faut que vous recommenciez")
        await cEp.send("C'est bon")
        Ep= ""
    await ctx.send("L'epouse se rendort")
    #Garde Du Corp

    await ctx.send("Le Garde du corp se reveille")

    GD=CheckNom("GardeDuCorp")
    while GD!="":
            overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            ctx.guild.me: discord.PermissionOverwrite(read_messages=True),
            GD: discord.PermissionOverwrite(read_messages=True)
            }

            channel1 = await ctx.guild.create_text_channel('Garde Du Corp', overwrites=overwrites)
            cGD = bot.get_channel(channel1.id)
            await cGD.send("Ecrivez le nom de la personne que vous voulez proteger par exemple:Toto Titi#1234")
            verif2 = False

            while verif2 == False:
                print("aaaa")

                def check(m):
                    return m.channel == cGD

                msg = await bot.wait_for("message", check=check)
                var = (msg.content)
                cible = ctx.guild.get_member_named(var)

                if cible != None:
                    for Jo in Liste2:
                        verif2 = True
                        print(2)
                        if Jo.Role=="GardeDuCorp":
                            if Jo.Distract != True:
                                for Jov in Liste2:
                                    if Jov.nom == cible:
                                        Jov.Proteger()
                            else:
                                await cGD.send( "Vous etes distrait par une jolie femme,vous ne pouvez donc pas proteger quelqu'un")
                if verif2==False:
                    await cGD.send("Il faut que vous recommenciez")
            await cGD.send("C'est bon")
            GD=""
    await ctx.send("Le Garde du corps se rendort")
    await ctx.send("Le Medecin se reveille")
    #Medecin

    MDC=CheckNom("Medecin")
    while MDC!="":
            overwrites = {
                ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
                ctx.guild.me: discord.PermissionOverwrite(read_messages=True),
                MDC: discord.PermissionOverwrite(read_messages=True)
            }

            channelM = await ctx.guild.create_text_channel('Medecin', overwrites=overwrites)
            cMDC= bot.get_channel(channelM.id)
            await cMDC.send("Ecrivez le nom de la personne que vous voulez soigner par exemple:Toto Titi#1234")
            verif3 = False

            while verif3 == False:
                print("aaaab")

                def check(m):
                    return m.channel == cMDC

                msg = await bot.wait_for("message", check=check)
                var = (msg.content)
                cible = ctx.guild.get_member_named(var)

                if cible != None:
                    for Jo in Liste2:
                        verif3 = True
                        print(2)
                        if Jo.Role=="Medecin":
                             if Jo.Distract!=True:
                                 for Jov in Liste2:
                                     if Jov.nom==cible:
                                         Jov.Soigner()
                             else:
                                await cMDC.send("Vous etes distrait par une jolie femme,vous ne pouvez donc pas soigner quelqu'un")
                    if verif3 == False:
                        await cMDC.send("Il faut que vous recommenciez")
                await cMDC.send("C'est bon")
            MDC=""
    await ctx.send("Le Medecin se rendort")

    #Le Parrain
    P = CheckNom("Parrain")
    await ctx.send("La Mafia se reveille,le Parrain donne ses ordres")
    while P != "":
        overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            ctx.guild.me: discord.PermissionOverwrite(read_messages=True),
            P: discord.PermissionOverwrite(read_messages=True)
        }

        channelP = await ctx.guild.create_text_channel('Mafia', overwrites=overwrites)
        cP = bot.get_channel(channelP.id)
        await cP.send("Ecrivez le nom de la personne que vous voulez tuez (cet ordre sera transmis au Mafieux) par exemple:Toto Titi#1234")
        verif4 = False

        while verif4 == False:
            print("aaaab")

            def check(m):
                return m.channel == cP

            msg = await bot.wait_for("message", check=check)
            var = (msg.content)
            cible = ctx.guild.get_member_named(var)

            if cible != None:
                for Jo in Liste2:
                    verif4 = True
                    print(2)
                    if Jo.Role == "Parrain":
                        if Jo.Distract == True:
                            for Jov in Liste2:
                                if Jov.Role=="Mafieu":
                                    if Jov.Distract==True:
                                        for JoMort in Liste2:
                                                if JoMort.nom==cible:
                                                    JoMort.Meurt()
                        else:
                         await cP.send( "Vous etes distrait par une jolie femme,vous ne pouvez donc pas donner d'ordre")
                if verif4 == False:
                    await cGD.send("Il faut que vous recommenciez")
            await cP.send("C'est bon")
        P = ""
    await ctx.send("Le/Les Mafieux executent les ordres")

    Ma= CheckNom("Mafieu")
    while Ma != "":
        await cP.send("Le Mafieu est entrain de tuer sa cible")
        verif5 = False
        while verif5 == False:
            print("aaaab")
            for Jo in Liste2:
                if Jo.Role == "Parrain":
                    if Jo.Distract == True:
                        while verif5 == False:
                            def check(m):
                                return m.channel == cP

                            msg = await bot.wait_for("message", check=check)
                            var = (msg.content)
                            cible = ctx.guild.get_member_named(var)

                            if cible != None:
                                for Jo in Liste2:
                                    verif5=True
                                    if Jo.Role == "Mafieu":
                                            if Jo.Distract != True:
                                                for Jov in Liste2:
                                                    if Jov.Role==cible:
                                                        Jov.Meurt()
                                            else:
                                                await cP.send(  "Vous etes distrait par une jolie femme,vous ne pouvez donc pas suivre les ordres")
                            if verif5 == False:
                                await cGD.send("Il faut que vous recommenciez")
                    else:
                        for JoV in Liste2:
                            if JoV.Role=="Mafieu":
                                 if JoV.Distract != True:
                                    if JoV.nom==cible:
                                        JoV.Meurt()
                                 else:
                                     await cP.send("Vous etes distrait par une jolie femme,vous ne pouvez donc pas suivre les ordres")
            await cP.send("C'est bon")
        Ma = ""
    #Faire le Jour + Maire
    #Vote Mort
    # Faire des tours qui se repetent




    @bot.command()
    async def reset(message):
        print("b")
        var = discord.utils.get(message.guild.roles, name="Joueur")
        await message.author.remove_roles(var)
        await channel.delete()
        await channelE.delete()
        await channelEp.delete()
        await channel1.delete()
        await channelM.delete()
        await channelP.delete()


bot.run("ODUwMDg3NDczODAzMDM0NjQ0.YLknpw.uVwTEABMHabBhZU_Rw0uQD8jAcY")

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
