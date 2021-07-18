class Match:
    def __init__(self, player1, player2, score_player1 = 0, score_player2 = 0):
        self.player1 = player1
        self.player2 = player2
        self.score_player1 = 0
        self.score_player2 = 0

    def serializer(self):
        data = {"player1": self.player1.serializer(),
                "player2": self.player2.serializer(),
                "score player 1": self.score_player1,
                "Score player 2": self.score_player2}
        return data



