from June2021 import Team
from June2021 import Match

names = ("Spain", "Sweden", "Poland", "Slovakia")

team1 = Team(names[0])
team1.make_team()
team2 = Team(names[1])
team2.make_team()
team3 = Team(names[2])
team3.make_team()
team4 = Team(names[3])
team4.make_team()


print("Results")

match1 = Match(team1, team2)
match1.play_match()
print(match1)

match2 = Match(team3,team4)
match2.play_match()
print(match2)

print("Leaderboard")

if match1.home_goals > match1.away_goals:
    print("Spain 3 points")
    print("Sweden 0 points")
elif match1.home_goals == match1.away_goals:
    print("Spain 1 points")
    print("Sweden 1 points")
else:
    print("Spain 0 points")
    print("Sweden 3 points")

if match2.home_goals > match2.away_goals:
    print("Poland 3 points")
    print("Slovakia 0 points")
elif match2.home_goals == match2.away_goals:
    print("Poland 1 points")
    print("Slovakia 1 points")
else:
    print("Poland 0 points")
    print("Slovakia 3 points")
