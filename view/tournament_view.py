import datetime
from utils import is_date_valid
from model.tournament_model import get_all_players

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
    #proposer input de date à date ?

def get_tournament_description():
    description = input("Entrez une description du tournoi : ")
    return description

def which_tournament_to_choose():
    tournament_choice = input("Quel tournoi souhaitez-vous reprendre ? : ")
    return tournament_choice

def print_home_menu():
    print("1: start new tournament")
    print("2: Reload a tournament")
    print("3: See reports and results")
    print("4: Quit")

def print_players_reports_menu():
    print("1: get all players in alphabetic order")
    """modele va donner l'info qui la transmet au controleur qui fait afficher par la view"""
    print("2: get players in elo ascending order")
    print("3: get players in elo descending order")

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
    all_players = get_all_players()
    print(all_players)



