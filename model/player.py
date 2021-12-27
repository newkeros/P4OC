from tinydb import TinyDB, Query


class Player:
    def __init__(
        self,
        first_name,
        last_name,
        elo,
        date_of_birth,
        player_gender,
        score=0,
        opponent=[],
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.elo = elo
        self.date_of_birth = date_of_birth
        self.player_gender = player_gender
        self.score = score
        self.opponent = opponent

    def first_name(self):
        return self.first_name

    def last_name(self):
        return self.last_name

    def get_elo(self):
        return self.elo

    def date_of_birth(self):
        return self.date_of_birth

    def player_gender(self):
        return self.player_gender

    def add_opponent(self, elo):
        self.opponent.append(elo)

    def serializer(self):
        data = {
            "first name": self.first_name,
            "last name": self.last_name,
            "elo": self.elo,
            "date of birth": self.date_of_birth,
            "player's gender": self.player_gender,
            "score": self.score,
            "opponent list": self.opponent,
        }
        return data

    def player_serializer(self):
        data = {
            "first name": self.first_name,
            "last name": self.last_name,
            "elo": self.elo,
            "date of birth": self.date_of_birth,
            "player's gender": self.player_gender,
        }
        return data

    def save_player(self):
        db = TinyDB("db_tournament.json", indent=4)
        tournaments = db.table("Players")
        tournaments.insert(self.player_serializer())
