from model.tournament_model import Tournament
from model.player import Player
from model.round import Round
from view.tournament_view import get_tournament_name, get_tournament_time_control, get_tournament_date
from view.player_view import print_player, get_player_info
from view.round_view import print_match_result, enter_score, print_final_round_score


players = [Player("Ranga", 34), Player("Grégory", 12), Player("Jean-Marie", 3), Player("toto", 100)]


class TournamentControler:
    def __init__(self):
        name = self.check_tournament_name()
        time_control = self.check_tournament_time_control()
        tournament_date = get_tournament_date()
        self.tournament = Tournament(name, time_control, tournament_date)
        # self.tournament = Tournament("test", "bullet") #BYPASS TOURNAMENT

        """for i in range(4):
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
        while time_control != "bullet" and time_control != "blitz" and time_control != "Coup rapide":
            print("Erreur de saisie, le type de partie doit être Bullet, Blitz ou Coup rapide")
            time_control = get_tournament_time_control()
        return time_control

    def check_tournament_date(self):
        tournament_date = get_tournament_date()
        while not tournament_date.isalpha():
            print("Erreur de saisie: la date ne peut contenir que des chiffres")
            tournament_date = get_tournament_date()
        return tournament_date


    def run_first_round(self):
        # algorithme pour créer les premier round
        self.tournament.players.sort(key=lambda x: x.elo)
        round1 = Round("1")
        self.tournament.add_round(round1)
        for i in range(2):
            round1.add_match(self.tournament.players[i], self.tournament.players[2 + i])

        for match in self.tournament.rounds[0].matchs:
            match.score_player1, match.score_player2 = self.handle_score()
            print_match_result(match)
            self.update_player_score(match)
        print_final_round_score(self.tournament.rounds[0].matchs, round1.number)


    def run_round(self, number):
        round = Round(str(number))
        self.tournament.add_round(round)
        pass

    def handle_score(self):
        score = enter_score()
        while score != "1" and score != "2" and score != "3":
            score = enter_score()

        if score == "1":
            return 1, 0
        elif score == "2":
            return 0, 1
        elif score == "3":
            return 0.5, 0.5

    def update_player_score(self, match):
        match.player1.score += match.score_player1
        match.player2.score += match.score_player2

