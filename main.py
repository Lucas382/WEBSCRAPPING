import requests
from bs4 import BeautifulSoup
from Partida import Partida
import pandas as pd
from matplotlib import pyplot as plt

Partida: Partida


def get_champion_list(span):
    list = []
    for item in range(len(span)):
        champion = span[item]
        list.append(champion.get('title'))
    return list


def main():
    partidas = []
    tabela_atual = 4

    # Pagina Url Desejada
    url = 'https://lol.fandom.com/wiki/LCK/2021_Season/Spring_Season/Match_History'

    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/96.0.4664.45 Safari/537.36 OPR/81.0.4196.60"}
    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')

    # Get all the table of matches
    tabela_toda = soup.body.findAll('tbody')
    tbody_tr = tabela_toda[tabela_atual].findAll('tr')

    for item in range(3, len(tbody_tr)):

        # Get the match given starting by 3, then get all td tags of this match
        tr_desejado = tbody_tr[item]
        td_desejado = tr_desejado.findAll('td')

        # Store the values needed for the dataclass
        data = td_desejado[0].get_text()
        patch = td_desejado[1].get_text()
        team_blue_side = td_desejado[2].find('a').get('title')
        team_red_side = td_desejado[3].find('a').get('title')
        winner = td_desejado[4].find('a').get('title')
        bans_blue_side = get_champion_list(td_desejado[5].findAll('span', class_='sprite champion-sprite'))
        bans_red_side = get_champion_list(td_desejado[6].findAll('span', class_='sprite champion-sprite'))
        picks_blue_side = get_champion_list(td_desejado[7].findAll('span', class_='sprite champion-sprite'))
        picks_red_side = get_champion_list(td_desejado[8].findAll('span', class_='sprite champion-sprite'))

        partidas.append(
            Partida(data, patch, team_blue_side, team_red_side, winner, bans_blue_side, bans_red_side, picks_blue_side,
                    picks_red_side))

    blue_aux = 0
    red_aux = 0
    winner_blue_side = []
    winner_red_side = []
    separation_by = 1

    chunk_list = [partidas[i:i + separation_by] for i in range(0, len(partidas), separation_by)]
    matches = []

    for chunk in chunk_list:
        for partida in chunk:
            if partida.get_winner() == 'red':
                red_aux += 1
            else:
                blue_aux += 1
        winner_red_side.append(red_aux)
        winner_blue_side.append(blue_aux)


    for i in range(1,201):
        matches.append(i)

    plt.plot(matches, winner_blue_side)
    plt.plot(matches, winner_red_side)
    plt.title("Relação de vitorias")
    plt.xlabel("Numero de partidas")
    plt.ylabel("Vitorias")
    plt.legend(["Time Azul","Time Vermelho"])
    plt.show()


if __name__ == '__main__':
    main()
