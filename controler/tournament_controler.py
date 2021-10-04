from model.tournament_model import Tournament
from model.player import Player
from model.round import Round
from view.tournament_view import get_tournament_name, get_tournament_time_control, get_tournament_date, \
    get_tournament_place, get_tournament_description, which_tournament_to_choose, print_home_menu, \
    print_players_reports_menu, user_input_menu
from view.player_view import print_player
from view.round_view import print_match_result, enter_score, print_final_round_score
from utils import is_date_valid
from model.match import Match
from tinydb import Query


players = [Player("Ranga", "Gonnage", 34, "04-03-1989", "Homme"), Player("Grégory", "Albert", 12, "04-03-1989", "Homme"),
           Player("Jean-Marie", "x", 3, "04-03-1989", "Homme"), Player("toto", "toto", 100, "04-03-1989", "Homme"),
           Player("bob", "test", 234, "04-03-1989", "Homme"),
           Player("Igor", "Kasparov", 2830, "04-03-1989", "Homme"),
           Player("guy", "montagné", 345, "04-03-1989", "Homme"),
           Player("jack", "black", 32, "04-03-1989", "Homme")]


class TournamentControler:
    def __init__(self):
        self.tournament = None

    def new_tournament(self):
        name = self.check_tournament_name()
        time_control = self.check_tournament_time_control()
        tournament_date = self.check_tournament_date()
        tournament_place = self.check_tournament_place()
        tournament_description = self.check_tournament_description()
        self.tournament = Tournament(name, time_control, tournament_date, tournament_place, tournament_description)
        # self.tournament = Tournament("test", "bullet") #BYPASS TOURNAMENT

        """for i in range(8):
            name, elo = get_player_info()
            player = Player(name, elo)
            self.tournament.add_player(player)
            player.save player à creer"""
        self.tournament.players = players
        Tournament.save(self.tournament.serializer())

    def print_player(self):
        """print_player(self.tournament.players)"""
        print_player(players)

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
        date = get_tournament_date()
        while not is_date_valid(date):
            print("La date n'a pas le bon format dd-mm-YYYY")
            date = get_tournament_date()
        return date

    def check_tournament_place(self):
        tournament_place = get_tournament_place()
        while not tournament_place.isalpha():
            print("Erreur de saisie, le lieu du tournoi ne peut contenir que des lettres")
            tournament_place = get_tournament_place()
        return tournament_place

    def check_tournament_description(self):
        tournament_description = get_tournament_description()
        """while not tournament_description.isalpha():
            print("Erreur de saisie, la description du tournoi ne peut contenir que des lettres")
            get_tournament_description()"""
        return tournament_description



    def run_first_round(self):
        # algorithme pour créer les premier round
        self.tournament.players.sort(key=lambda x: x.elo) #trier les joueurs par elo
        round1 = Round("1") #nom du first round
        self.tournament.add_round(round1) #ajoute le round à la liste
        for i in range(4):
            round1.add_match(self.tournament.players[i], self.tournament.players[4 + i]) #1er du haut du tableau contre 5ème

        for match in self.tournament.rounds[0].matchs: #matching de joueurs
            match.score_player1, match.score_player2 = self.handle_score()
            print_match_result(match)
            self.update_player_score(match)
        print_final_round_score(self.tournament.rounds[0].matchs, round1.number)


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



    def get_player(self):
        players = list()

        for player in self.tournament.players:
            players.append(player)

        players.sort(key=lambda x: x.elo, reverse=True)
        players.sort(key=lambda x: x.score, reverse=True)

        return players


    def run_round(self, round_number):
        round = Round(str(round_number))
        self.tournament.add_round(round)
        players = self.get_player()


        i = 0

        while len(players) > 0:
            player1 = players[i]
            player2 = players[i + 1]

            while player2.elo in player1.opponent:
                try:
                    i += 1
                    player2 = players[i + 1]
                except IndexError:
                    player2 = players[1]
                    i = 0
                    break

            round.add_match(player1, player2)
            del players[0]
            del players[i]

            i = 0

        for match in self.tournament.rounds[round_number - 1].matchs:
            match.score_player1, match.score_player2 = self.handle_score()
            print_match_result(match)
            self.update_player_score(match)
        print_final_round_score(self.tournament.rounds[round_number - 1].matchs, round.number)


    def reload_tournament(self, tournament_name):
        self.tournament = Tournament.deserializer(tournament_name)
        rounds_to_run = 4 - (len(self.tournament.rounds))

        if rounds_to_run == 4:
            self.run_first_round()
            for i in range(2, 5):
                self.run_round(i)
        else:
            for i in range(rounds_to_run):
                self.run_round(5-rounds_to_run+i)

    def search_tournament(self):
        names = Tournament.get_ongoing_tournaments()
        return(names)

    def choose_tournament(self):
        tournament_choice = which_tournament_to_choose()
        if tournament_choice == 1:
            return
        elif tournament_choice == 2:
            return
        elif tournament_choice == 3:
            return

    def menu_home(self):
        is_app_run = True
        while is_app_run:
            print_home_menu()
            answer = user_input_menu()
            if answer == "1":
                self.new_tournament()
                self.run_first_round()
                for i in range(2, 5):
                    self.run_round(i)
            elif answer == "2":
                names = Tournament.get_ongoing_tournaments()
                for i in range(len(names)):
                    print(f"{i} - {names[i]}")
                choose_tournament = which_tournament_to_choose()
                while True:
                    try:
                        tournament_number = int(choose_tournament)
                        if tournament_number >= 0 and tournament_number < len(names):
                            self.reload_tournament(names[tournament_number])
                        else:
                            choose_tournament = input("Erreur : Choisir le numéro du tournoi : ")
                    except ValueError:
                        choose_tournament = input("Erreur : Choisir le numéro du tournoi : ")
                print(names[tournament_number])
            elif answer == "3":
                print_players_reports_menu()
            elif answer == "4":
                is_app_run = False
            else:
                print("error input")




