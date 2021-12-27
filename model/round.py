from model.match import Match


class Round:
    def __init__(self, number):
        self.number = number
        self.matchs = []

    def add_match(self, player1, player2):  # 1
        match = Match(player1, player2)
        self.matchs.append(match)
        player1.add_opponent(player2.get_elo())
        player2.add_opponent(player1.get_elo())

    def add_reload_match(self, match):
        self.matchs.append(match)

    def serializer(self):
        data = {
            "number": self.number,
            "matchs": [match.serializer() for match in self.matchs],
        }
        return data
