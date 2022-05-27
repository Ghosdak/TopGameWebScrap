import requests
import lxml
from bs4 import BeautifulSoup

url = ("https://steamcharts.com/")
user_agent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43")
headers = {
    "User-Agent": user_agent,
}
response = requests.get(url, headers=headers)
response.raise_for_status()
data = response.text
soup = BeautifulSoup(data, "lxml")
top10_games = [game.getText().strip() for game in soup.select("#top-games a")]
top10_players = [game.getText() for game in soup.select('#top-games .num')[::3]]
top10_peak_players = [game.getText() for game in soup.select('#top-games .num')[1::3]]
top10_hours_played = [game.getText() for game in soup.select('#top-games .num')[2::3]]

with open('steam-top-games.csv', mode='w') as file:
    file.writelines('Top-game,Current-players,Peak-players,Hours-played\n')
    for n in range(len(top10_games)):
        file.writelines(f'{top10_games[n]},{top10_players[n]},{top10_peak_players[n]},{top10_hours_played[n]}\n')
