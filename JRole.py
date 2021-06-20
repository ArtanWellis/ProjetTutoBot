import discord
from discord.ext import commands
import random
from discord.ext.commands import Bot


class JRole:
    def __init__(self, role, no):
        self.nom = no
        self.Role = role
        self.Mort = False
        self.Protect = False
        self.Soin = False
        self.Distract = False

    def getnom(self):
        return (self.nom)

    def Proteger(self):
        self.Protect = True
    def Soigner(self):
        self.Soin = True
    def Distraire(self):
        self.Distract=True
    def Meurt(self):
        self.Mort=True
