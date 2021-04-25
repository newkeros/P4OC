import os


def enter_score():
    score = input("Entrez le score (1 : victoire du joueur 1 / 2 : victoire du joueur 2 / 3 : égalité")
    return score

def print_match_result(match):
    print(f"{match.player1.name} : {match.score_player1}", f"\n{match.player2.name} : {match.score_player2}")

def print_final_round_score(matchs, number):
    os.system("clear")
    print(f"FINAL SCORES ROUND {number}: ")
    for match in matchs
        print(f"{match.player1.name} : {match.player1.score}")
        print(f"{match.player2.name} : {match.player2.score}")