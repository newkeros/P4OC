import datetime
from utils import is_date_valid
from model.tournament_model import Tournament


def get_tournament_name():
    name = input("Enter the tournament name : ")
    return name


def get_tournament_time_control():
    time_control = input("Enter time control (Bullet/Blitz/Coup rapide) : ")
    return time_control


def get_tournament_place():
    tournament_place = input("Enter the tournament place : ")
    return tournament_place


def get_tournament_date():
    tournament_date = input("Entrez la date du tournoi : ")
    return tournament_date
    # proposer input de date à date ?


def get_tournament_description():
    description = input("Entrez une description du tournoi : ")
    return description


def which_tournament_to_choose():
    tournament_choice = input("Quel tournoi souhaitez-vous selectionner ? : ")
    return tournament_choice


def print_home_menu():
    print("1: start new tournament")
    print("2: Reload a tournament")
    print("3: See reports and results")
    print("4: Quit")


def print_reports_menu():
    print("1: Players ordered by name")
    print("2: Players ordered by elo")
    print("3: Players list from a tournament")
    print("4: Players from a tournament ordered by elo")
    print("5: All tournaments list")
    print("6: all rounds list")
    print("7: All matchs list")


def user_input_menu():
    answer = input("Faites votre choix : ")
    return answer


def continue_tournament():
    name = input("Voulez-vous continuer le tournoi (Oui/Non) : ")
    return name


def tournament_selection_for_player_reports():
    answer = input("De quel tournoi voulez vous afficher la liste des joueurs ? ")
    return answer


def print_all_players():
    all_players = Tournament.get_all_players()
    print(all_players)


def print_players_reports_menu():
    return None


def display_match(rounds):
    for round in rounds:
        print(f"Numero du round : {round['number']}")
        print("-------- Matchs --------")
        for index, match in enumerate(round["matchs"]):
            print(f"{index + 1} : {match['player1']['first name']} VS {match['player2']['first name']}")


def display_round(rounds):
    for round in rounds:
        print(f"Numero du round : {round['number']}")

