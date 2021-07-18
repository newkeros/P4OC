def get_player_first_name():
    first_name = input("Enter the player first name : ")
    return first_name

def get_player_last_name():
    last_name = input("Enter the player name : ")
    return last_name

def get_player_elo():
    elo = input("Enter the player elo : ")
    return elo

def get_date_of_birth():
    date_of_birth = input("Entrez la date de naissance : ")
    return date_of_birth

def get_player_gender():
    player_gender = input("Le joueur est-il un homme ou une femme ? (dans le format H/F)")
    return player_gender


def print_player(players):
    for player in players:
        print("--------------------")
        print(f"first name : {player.first_name}")
        print(f"last name : {player.last_name}")
        print(f"elo : {player.elo}")
        print(f"date of birth : {player.date_of_birth}")
        print(f"player gender : {player.player_gender}")
        print("--------------------")
