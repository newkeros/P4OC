import datetime

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
    date_data = input("Entrez la date dans le format AAAA-MM-JJ : ")
    year, month, day = map(int, date_data.split('-'))
    tournament_date = datetime.date(year, month, day)
    return tournament_date
    #proposer input de date à date ?

def get_tournament_description():
    description = input("Entrez une description du tournoi: ")
    return description

