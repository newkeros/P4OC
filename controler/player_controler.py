from utils import is_date_valid
from view.player_view import get_date_of_birth, get_player_first_name, get_player_last_name, get_player_elo, get_player_gender


def get_and_check_date():
    date = get_date_of_birth
    while not is_date_valid(date):
        print("La date n'a pas le bon format dd-mm-YYYY")
        date = get_date_of_birth()
    return date

def get_and_check_first_name():
    first_name = get_player_first_name()
    while not first_name.isalpha():
        print("Le prénom ne peut contenir que des lettres")
        first_name = get_player_first_name()
    return first_name

def get_and_check_last_name():
    last_name = get_player_last_name()
    while not last_name.isalpha():
        print("Le nom de famille ne peut contenir que des lettres")
        last_name = get_player_first_name()
    return last_name

def get_and_check_elo():
    elo = get_player_elo()
    while elo.isalpha():
        print("Le classement elo ne peut contenir que des chiffres")
        elo = get_player_elo()
    return elo

def get_and_check_player_gender():
    player_gender = get_player_gender()
    player_gender = player_gender.lower()
    while player_gender != "Homme" and player_gender != "Femme":
        print("Le genre du joueur ne peut être que Homme ou Femme")
        player_gender = get_player_gender()
    return player_gender
