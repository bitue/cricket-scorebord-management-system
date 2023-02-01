class Team :
    def __init__(self, name) -> None:
        self.teamName = name 
        self.players =[]

    def entry_players(self, player):
        self.players.append(player)


class Player :
    def __init__(self, name ,age , team) -> None:
        self.playerName = name 
        self.strikeRate = 0.0 
        self.run_bat = 0 
        self.ball_bat  =0 
        self.run_ball =0 
        self.wicket =0 
        self.sixes =0 
        self.fours =0 
        self.strike_rate =0.0 
        self.overall_strike_rate =0.0 
        self.age =age 
        team.players.append(self)


class Innings :
    def __init__(self, team1, team2, battingTeam, bowlingTeam) -> None:
        self.teamOne = team1
        self.teamTwo =team2
        


Bangladesh = Team("Bangladesh")
India = Team("India")

Tamim = Player("Tamim Iqbal", 31, Bangladesh)
Kohli = Player("Virat Kohli", 32, India)

Rohit = Player("Rohit Sharma", 32, India)
Shakib = Player("Shakib Al Hassan", 30, Bangladesh)

Bumrah = Player("Bumrah", 32, India)
Taskin = Player("Taskin Ahmed", 30, Bangladesh)

for p in Bangladesh.players :
    print(p.playerName)


        
     
        


