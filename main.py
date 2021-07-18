from controler.tournament_controler import TournamentControler

tournamentControler = TournamentControler()
tournamentControler.print_player()
tournamentControler.run_first_round()
for i in range(2,5):
      tournamentControler.run_round(i)
tournamentControler.tournament_db()