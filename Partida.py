from dataclasses import dataclass, field

@dataclass
class Partida:
    date: str = ""
    patch: str = ""
    team_blue_side: str = ""
    team_red_side: str = ""
    winner: str = ""
    bans_blue_side: list[str] = field(default_factory=list)
    bans_red_side: list[str] = field(default_factory=list)
    picks_blue_side: list[str] = field(default_factory=list)
    picks_red_side: list[str] = field(default_factory=list)


    def __str__(self):
        return f'{self.date},{self.patch},{self.team_blue_side},{self.team_red_side},{self.winner},{self.bans_blue_side},' \
               f'{self.bans_red_side},{self.picks_blue_side},{self.picks_red_side}'

    def get_winner(self):
        if self.winner == self.team_blue_side:
            print(f'{self.winner} Venceu do lado azul')
            print(f'Usando {self.picks_blue_side}')
            print(f'Contra {self.picks_red_side}')
        else:
            print(f'{self.winner} Venceu do lado vermelho')
            print(f'Usando {self.picks_red_side}')
            print(f'Contra {self.picks_blue_side}')
