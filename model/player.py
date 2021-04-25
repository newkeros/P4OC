class Player:
    def __init__(self, name, elo):
        self.name = name
        self.elo = elo
        self.score = 0

        def __str__(self):
            return self.name