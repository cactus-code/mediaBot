import re
import discord
from discord.ext.commands import Bot
import youtube_dl
import asyncio
from musicbot.opus_loader import load_opus_lib
load_opus_lib()
from musicbot.downloader import search
from musicbot.downloader import download
from steambot.steam_client import list_user_games
from steambot.steam_client import get_user_name
try: #Tries to import arduino module and connect to board
    from arduinobot.main import set_rgb_led
    print("Booted with arduino library.")
except:
    print("Booted without arduino library.")
    pass

token = "MzIwODY5NjAwNDUzNzIyMTEy.DB074Q.FMXkk0_CnuBuvno3eqwe0d2dnUs"
game = "Google: The Game"

media_bot = Bot(command_prefix="?")

playlist = []

@media_bot.event
async def on_ready():
    #This runs when the bot boots up
    print("Client logged in")
    print('Name:{}'.format(media_bot.user.name))
    print('ID:{}'.format(media_bot.user.id))
    print(discord.__version__)
    print('Playing:{}'.format(game))
    await media_bot.change_presence(game=discord.Game(name=game))

@media_bot.command(pass_context=True)
async def rgb(ctx,*args):
    red = int(args[0])
    green = int(args[1])
    blue = int(args[2])
    set_rgb_led(red,green,blue)

@media_bot.event
async def on_message(message):
    if not (message.author).bot:
        if message.content.startswith('?play'):
            video = search(message.content)
            #download(video)
            author_channel = (message.author).voice_channel
            voice = await media_bot.join_voice_channel(author_channel)
            player = await voice.create_ytdl_player(video)
            player.start()
        if message.content.startswith('?shutdown'):
            await media_bot.close()
        if message.content.startswith('?steam_list_games'):
            content = message.content
            content = content.replace('?steam_list_games ','')
            games_list = list_user_games(content)
            username = get_user_name(content)
            await media_bot.send_message(message.channel,(message.author).mention + ' Games owned by Steam User: {} are: {}'.format(username,games_list))
    await media_bot.process_commands(message)
           
media_bot.run(token)
