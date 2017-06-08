import urllib.request
import urllib.parse
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
try: #Tries to import arduino module and connect to board
    from arduinobot.main import notification_blink
    print("Booted with arduino library.")
except:
    print("Booted without arduino library.")
    pass


token = "your bot token here"
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

@media_bot.event
async def on_message(message):
    if not (message.author).bot:
        try:
            notification_blink()
        except:
            pass
        if message.content.startswith('?play'):
            video = search(message.content)
            download(video)
            #author_channel = (message.author).voice_channel
            #voice = await media_bot.join_voice_channel(author_channel)
            #player = await voice.create_ytdl_player(link)
            #player.start()
        if message.content.startswith('?shutdown'):
            await media_bot.close()
        if message.content.startswith('?steam_list_games'):
            content = message.content
            content = content.replace('?steam_list_games ','')
            games_list = list_user_games(content)
            await media_bot.send_message(message.channel,(message.author).mention + ' Games owned by ID: {} are: {}'.format(content,games_list))
           
media_bot.run(token)
