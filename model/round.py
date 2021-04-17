class Round:
    def __init__(self, number):
        self.number = number
        self.matchs = []

    def add_match(self, player1, player2):  # 1
        match = Match(player1, player2)
        self.matchs.append(match)

    def add_match2(self, match):  # 2
        self.matchs.append(match)