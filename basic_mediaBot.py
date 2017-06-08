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

token = "MzIwODY5NjAwNDUzNzIyMTEy.DBV5hQ.E8X1gLcD5Cocpry9opvoah3HZ9g"
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
        if message.content.startswith('?play'):
            query = message.content.lower()
            query = query.replace('?play ','')
            query_string = urllib.parse.urlencode({"search_query" : query})
            html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
            search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
            video = "http://www.youtube.com/watch?v=" + search_results[0]
            author_channel = (message.author).voice_channel
            voice = await media_bot.join_voice_channel(author_channel)
            player = await voice.create_ytdl_player(video)
            player.start()
        if message.content.startswith('?shutdown'):
            await media_bot.close()
           
media_bot.run(token)
