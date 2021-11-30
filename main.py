import requests
from bs4 import BeautifulSoup

url = 'https://lol.fandom.com/wiki/LCK/2021_Season/Spring_Season/Match_History'

headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 OPR/81.0.4196.60"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')

# partidas = soup.find('table', class_='wikitable hoverable-multirows mhgame sortable plainlinks column-show-hide-1 jquery-tablesorter')

partida_blue = soup.findAll('tr', class_='mhgame-blue multirow-highlighter')
partida = partida_blue[0]

bans = partida.findAll('td', class_='mhgame-bans')
bans_l = bans[0]
bans_r = bans[1]

# picks = partida.findAll('td')
# pick_l = picks[7]


champions_ban_l = bans_l.findAll('span', class_='sprite champion-sprite')
champions_ban_r = bans_r.findAll('span', class_='sprite champion-sprite')

title_l = []
title_r = []
for boneco in range(len(champions_ban_l)):
    campeao_l = champions_ban_l[boneco]
    campeao_r = champions_ban_r[boneco]
    title_l.append(campeao_l.get('title'))
    title_r.append(campeao_r.get('title'))

print(f'Campeos banidos Esquerda{title_l}')
print(f'Campeos banidos Direita{title_r}')

