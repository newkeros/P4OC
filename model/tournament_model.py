from tinydb import TinyDB, Query
from model.player import Player
from model.round import Round
from model.match import Match


class Tournament:
    def __init__(self, name, time_control, date, place, description):
        self.name = name
        self.time_control = time_control
        self.date = date
        self.place = place
        self.description = description
        self.players = []
        self.rounds = []

    def add_player(self, player):
        self.players.append(player)

    def add_round(self, round):
        self.rounds.append(round)

    def serializer(self):
        data = {
            "name": self.name,
            "time control": self.time_control,
            "date": self.date,
            "place": self.place,
            "description": self.description,
            "players": [player.serializer() for player in self.players],
            "rounds": [round.serializer() for round in self.rounds],
        }
        return data

    @staticmethod
    def save(serialized_tournament):
        db = TinyDB("db_tournament.json", indent=4)
        tournaments = db.table("Tournaments")
        tournaments.insert(serialized_tournament)

    @staticmethod
    def update(serialized_tournament, name):
        db = TinyDB("db_tournament.json", indent=4)
        tournaments = db.table("Tournaments")
        tournament = Query()
        tournaments.update(serialized_tournament, tournament.name == name)

    @staticmethod
    def deserializer(name):
        db = TinyDB("db_tournament.json", indent=4)
        tournaments = db.table("Tournaments")
        tournament = Query()

        tournament = tournaments.search(tournament.name == name)[0]
        reload_tournament = Tournament(
            tournament["name"],
            tournament["time control"],
            tournament["place"],
            tournament["date"],
            tournament["description"],
        )

        for player in tournament["players"]:
            reload_player = Player(
                player["first name"],
                player["last name"],
                player["elo"],
                player["date of birth"],
                player["player's gender"],
                player["score"],
                player["opponent list"],
            )
            reload_tournament.add_player(reload_player)

        for round in tournament["rounds"]:
            reload_round = Round(round["number"])
            for match in round["matchs"]:
                player1 = Player(
                    match["player1"]["first name"],
                    match["player1"]["last name"],
                    match["player1"]["elo"],
                    match["player1"]["date of birth"],
                    match["player1"]["player's gender"],
                    match["player1"]["score"],
                    match["player1"]["opponent list"],
                )
                player2 = (
                    match["player2"]["first name"],
                    match["player2"]["last name"],
                    match["player2"]["elo"],
                    match["player2"]["date of birth"],
                    match["player2"]["player's gender"],
                    match["player2"]["score"],
                    match["player2"]["opponent list"],
                )
                reload_match = Match(
                    player1, player2, match["score player 1"], match["Score player 2"]
                )
                reload_round.add_reload_match(reload_match)
            reload_tournament.add_round(reload_round)
        return reload_tournament

    @staticmethod
    def get_ongoing_tournaments():
        db = TinyDB("db_tournament.json", indent=4)
        tournaments = db.table("Tournaments")
        tournaments = tournaments.all()
        tournament_names = []
        for tournament in tournaments:
            if len(tournament["rounds"]) < 4:
                tournament_names.append(tournament["name"])
        return tournament_names

    @staticmethod
    def get_all_tournaments():
        db = TinyDB("db_tournament.json", indent=4)
        tournaments = db.table("Tournaments")
        tournaments = tournaments.all()
        tournament_names = []
        for tournament in tournaments:
            tournament_names.append(tournament["name"])
        return tournament_names

    @staticmethod
    def get_all_players():
        db = TinyDB("db_tournament.json", indent=4)
        players = db.table("Players")
        return players.all()

    @staticmethod
    def get_tournament_players():  # récupérer le nom d'un tournoi précis (faire comme le désiarializer)
        db = TinyDB("db_tournament.json", indent=4)
        players = db.table("Tournaments")
        players = players.all()
        players_names = []
        for player in players:
            players_names.append(player["last name"])
        return players_names

    @staticmethod
    def print_tournament(self, tournament_name):
        self.tournament = Tournament.deserializer(tournament_name)

    def get_user_input(range):
        input_user = input("Entrer votre choix  : ")
        while not int(input_user) > 0 or not int(input_user) <= range:
            input_user = input("Entrer votre choix  : ")
        return int(input_user)

    @staticmethod
    def get_tournament_player(name):
        db = TinyDB("db_tournament.json", indent=4)
        tournaments = db.table("Tournaments")
        tournament = Query()

        tournament = tournaments.search(tournament.name == name)[0]

        return tournament["players"]

    @staticmethod
    def get_tournament_rounds(name):
        db = TinyDB("db_tournament.json", indent=4)
        tournaments = db.table("Tournaments")
        tournament = Query()

        tournament = tournaments.search(tournament.name == name)[0]
        return tournament[
            "rounds"
        ]  # créer à part un display round comme pour le display player

    @staticmethod
    def get_tournament_matchs(name):
        db = TinyDB("db_tournament.json", indent=4)
        tournaments = db.table("Tournaments")
        tournament = Query()

        tournament = tournaments.search(tournament.name == name)[0]
        matchs = []
        for round in tournament[
            "rounds"
        ]:  # dans chaque round append match. Puis return matchs à la fin
            matchs.append(round["matchs"])
        return matchs
