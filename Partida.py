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
            return 'blue'
        else:
            return 'red'

    def champion_win_side(self,champion):
        if champion in self.picks_blue_side and self.winner == self.team_blue_side:
            return "blue"

        elif champion in self.picks_red_side and self.winner == self.team_red_side:
            return "red"

        else:
            "none"
