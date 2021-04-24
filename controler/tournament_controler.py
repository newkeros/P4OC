from model.tournament_model import Tournament
from model.player import Player
from model.round import Round
from view.tournament_view import get_tournament_name, get_tournament_time_control
from view.match import enter_score
from view.player import print_player


players = [Player("Ranga", 1), Player("Grégory", 2)]


class TournamentControler:
    def __init__(self):
        name = self.check_name()
        time_control = self.check_tournament_time_control()
        self.tournament = Tournament(name, time_control)

        """for i in range(2):
            name, elo = get_player_info()
            player = Player(name, elo)
            self.tournament.add_player(player)"""
        self.tournament.players = players

    def print_player(self):
        print_player(self.tournament.players)

    def check_tournament_name(self):
        tournament_name = get_tournament_name()
        while not tournament_name.isalpha():
            print("Erreur de saisie, le nom du tournoi ne peut contenir que des lettres")
            tournament_name = get_tournament_name()
        return tournament_name

    def check_tournament_time_control(self):
        time_control = get_tournament_time_control()
        time_control = time_control.lower()
        while time_control != "bullet" and time_control != "blitz" and time_control != "Coup rapide"
            print("Erreur de saisie, le type de partie doit être Bullet, Blitz ou Coup rapide")
            time_control = get_tournament_time_control()
        return time_control


    def run_first_round(self):
        # algorithme pour créer les premier round
        self.tournament.player.sort(key=lambda x: x.elo)
        round1 = Round("1")
        self.tournament.add_round(round1)
        for i in range(4):
            round1.add_match(self.tournament.player[i], self.tournament.player[4 + i])

        for match in self.tournament.round[0].matchs:
            enter_score()

    def first_round_results(self):
        for match in self.tournament.round[0].matchs:
            """entrer score pour le premier match. """
