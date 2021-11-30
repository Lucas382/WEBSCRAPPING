import requests
from bs4 import BeautifulSoup
from Partida import Partida


def get_champion_list(span):
    list = []
    for item in range(len(span)):
        champion = span[item]
        list.append(champion.get('title'))
    return list


Partida: Partida
partidas = []

#Pagina Url Desejada
url = 'https://lol.fandom.com/wiki/LCK/2021_Season/Spring_Season/Match_History'
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/96.0.4664.45 Safari/537.36 OPR/81.0.4196.60"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')

#Get all the table of matches
tabela_toda = soup.body.findAll('tbody')
tbody_tr = tabela_toda[4].findAll('tr')

#Get the match given starting by 3 ending by 202, then get all td tags of this match
tr_desejado = tbody_tr[7]
td_desejado = tr_desejado.findAll('td')

#Store the values needed for the dataclass
data = td_desejado[0].get_text()
patch = td_desejado[1].get_text()
team_blue_side = td_desejado[2].find('a').get('title')
team_red_side = td_desejado[3].find('a').get('title')
winner = td_desejado[4].find('a').get('title')
bans_blue_side = get_champion_list(td_desejado[5].findAll('span', class_='sprite champion-sprite'))
bans_red_side = get_champion_list(td_desejado[6].findAll('span', class_='sprite champion-sprite'))
picks_blue_side = get_champion_list(td_desejado[7].findAll('span', class_='sprite champion-sprite'))
picks_red_side = get_champion_list(td_desejado[8].findAll('span', class_='sprite champion-sprite'))


def main():
    partidas.append(Partida(data, patch, team_blue_side, team_red_side, winner, bans_blue_side, bans_red_side, picks_blue_side, picks_red_side))
    for partida in partidas:
        if partida.winner == partida.team_blue_side:
            print(f'{partida.winner} Venceu do lado azul')
            print(f'Usando {picks_blue_side}')
            print(f'Contra {picks_red_side}')
        else:
            print(f'{partida.winner} Venceu do lado vermelho')
            print(f'Usando {picks_red_side}')
            print(f'Contra {picks_blue_side}')


if __name__ == '__main__':
    main()
