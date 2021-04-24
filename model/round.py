from model.match import Match

class Round:
    def __init__(self, number):
        self.number = number
        self.matchs = []

    def add_match(self, player1, player2):  # 1
        match = Match(player1, player2)
        self.matchs.append(match)
