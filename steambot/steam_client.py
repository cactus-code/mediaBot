import steam
from steam.api import interface

API_KEY = 'E0CA4AA7D95371E3F5944D5155FCB245'
steam.api.key.set(API_KEY)

def list_user_games(STEAM_ID):
    games = interface('IPlayerService').GetOwnedGames(steamid=STEAM_ID, include_appinfo=1)
    game_count = games['response']['game_count']
    user_games = []
    for i in range(0,game_count):
        data = (games['response']['games'][i])
        user_games.append(data['name'])
    user_games = str(user_games)
    replace = ["[","]","'"]
    for i in range(0,len(replace)):
        user_games = user_games.replace(replace[i],'')
    return user_games
