import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
@bot.event
async def on_message(message):
    if 'ugly' in message.content.lower():
        if message.author.id != bot.user.id:
            await message.channel.send("UR MOM UGLY IN BED AHAHAHAHA")

    if 'stinky' in message.content.lower():
        if message.author.id != bot.user.id:
            await message.channel.send("UR MOM STINKY IN BED AXAXAXA")

    if 'smelly' in message.content.lower():
        if message.author.id != bot.user.id:
            await message.channel.send("UR MOM BREATH SMELLY AHAHAHAHAHA NOOB UGLY")

    if 'wow' in message.content.lower():
        if message.author.id != bot.user.id:
            await message.channel.send("WOW? MORE LIKE WORLD OF WFAGGOTS NOOB AHAHAHAHAHA")

    if 'league of legends' in message.content.lower():
        if message.author.id != bot.user.id:
            await message.channel.send("LEAGUE OF LEGENDS? LUL MORE LIKE LEAGUE OF NIGGERS HAHAAHAHAHAHAHA")

    if 'lol' in message.content.lower():
        if message.author.id != bot.user.id:
            await message.channel.send("LOL? MORE LIKE LEAGUE OF BITCH AHAHAHAHA")

    if 'my nama' in message.content.lower():
        if message.author.id != bot.user.id:
            await message.channel.send(":regional_indicator_j: :regional_indicator_e: :regional_indicator_f: :regional_indicator_f:")
    
    if 'ugalee' in message.content.lower():
        if message.author.id != bot.user.id:
            await message.channel.send("UR MOM UGALEE IN BED")

    if 'no u' in message.content.lower():
        if message.author.id != bot.user.id:
            await message.channel.send("NO UR MOM PUSSY")

    if 'crikey' in message.content.lower():
        if message.author.id != 297111993352060948: #shk
            await message.channel.send("FUCK U THATS SHK'S WORD NOT YOURS PUSSY SMALL DICK LOOKIN ASS")

    if 'pride' in message.content.lower():
        if message.author.id == 312670966188867585: #benyameen
            await message.channel.send("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
            
bot.run("MzgwMzk0Nzg4NzY1MzAyNzg0.DO3-LQ.VPlZVCU7RGXjQvsP10v8055bHQA")
