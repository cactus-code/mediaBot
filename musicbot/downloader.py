import youtube_dl
import urllib.request
import urllib.parse
import re

class MyLogger():
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def search(message):
    query = message.lower()
    query = query.replace('?play ','')
    query_string = urllib.parse.urlencode({"search_query" : query})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    video = "http://www.youtube.com/watch?v=" + search_results[0]
    return video

global ydl_opts
ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'logger': MyLogger(),
        'outtmpl': 'music/audio.mp3',
    }

def download(video):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(video)
