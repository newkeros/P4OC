class Player:
    def __init__(self, name, elo):
        self.name = name
        self.elo = elo
        self.score = 0
        self.opponent = []

        def __str__(self):
            return self.name

        def add_opponent(self, elo):
            self.opponent.append(elo)

        def get_elo(self):
            return self.elo