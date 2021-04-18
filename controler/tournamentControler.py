from model.tournamentmodel import Tournament
from model.player import Player
from model.round import Round
from model.match import Match
from view.match import get_tournament_info
from view.match import enter_score
from view.player import print_player


players = [Player("Ranga", 1), Player("Grégory", 2)]


class TournamentControler:
    def __init__(self):
        name, time_control = get_tournament_info()
        self.tournament = Tournament(name, time_control)

        """for i in range(2):
            name, elo = get_player_info()
            player = Player(name, elo)
            self.tournament.add_player(player)"""
        self.tournament.players = players

    def print_player(self):
        print_player(self.tournament.players)

    def run_first_round(self):
        # algorithme pour créer les premier round
        self.tournament.player.sort(key=lambda x: x.elo)
        round1 = Round("1")
        self.tournament.add_round(round1)
        for i in range(4):
            round1.add_match(self.tournament.player[i], self.tournament.player[4 + i])

        for match in self.tournament.round[0].matchs:
            enter_score()