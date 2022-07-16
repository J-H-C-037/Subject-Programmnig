import random

"""

Player:
- position: goalkeeper, defender, midfielder, forward
- ability: 1 - 10

"""


class Player:
    def __init__(self, position: str, ability: int):
        self.position = position
        self.ability = ability

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, p):
        if p.lower() not in ["goalkeeper", "defender", "midfielder", "forward"]:
            raise ValueError("No such position")
        else:
            self.__position = p

    @property
    def ability(self):
        return self.__ability

    @ability.setter
    def ability(self, a):
        if type(a) != int:
            raise TypeError("It must be an interger")
        elif a > 10 or a < 1:
            raise ValueError("It must be between 0 and 10")
        else:
            self.__ability = a


"""

Team:

- name
- starting: 11 starting players: one goalkeeper, any number of defenders, midfielders or forwards (at lesat one for each position)
- substitute: 11 substitute players
- points: 0

"""


class Team:
    def __init__(self, name):
        self.name = name
        self.starting = []
        self.substitute = []
        self.points = 0

    def call_player(self):
        players = []
        positions = ["goalkeeper", "defender", "midfielder", "forward"]
        players.append(Player("goalkeeper", random.randint(1, 10)))
        players.append(Player("goalkeeper", random.randint(1, 10)))
        players.append(Player("defender", random.randint(1, 10)))
        players.append(Player("midfielder", random.randint(1, 10)))
        players.append(Player("forward", random.randint(1, 10)))

        for i in range(22 - 5):
            players.append(Player(positions[random.randint(0, 3)], random.randint(1, 10)))

        return players

    def make_team(self):
        players = self.call_player()
        ordered_players = []
        highest = 10
        for round in range(1, 10):
            for player in players:
                if player.ability == highest:
                    ordered_players.append(player)
            highest -= 1
        self.starting = ordered_players[0:10]
        self.subtitute = ordered_players[11:-1]

        goalkeeper = 0
        second_goalkeeper = 999
        for player in self.starting:
            if player.position == "goalkeeper":
                goalkeeper += 1
                if goalkeeper == 2:
                    second_goalkeeper = self.starting.index(player)
        change = 999
        if goalkeeper == 0:
            for player in self.subtitute:
                if player.position == "goalkeeper" and change == 999:
                    change = self.subtitute.index(player)
            self.starting = ordered_players[0:9] + ordered_players[11 + change:11+change]
            self.subtitute = ordered_players[11:11 + change] + ordered_players[11 + 1 + goalkeeper:-1]
        elif goalkeeper == 2:
            for player in self.subtitute:
                if player.position != "goalkeeper" and change == 999:
                    change = self.subtitute.index(player)
            self.starting = ordered_players[0:second_goalkeeper] + ordered_players[1 + second_goalkeeper: 10] + ordered_players[change + 11:change+11]
            self.subtitute = ordered_players[11:11 + change] + ordered_players[11 + 1 + change:-1] + ordered_players[second_goalkeeper:second_goalkeeper]

    def abilities(self):
        sum_goalkeeper = 0
        sum_defenders = 0
        sum_midfielders = 0
        sum_forwards = 0

        for player in self.starting:
            if player.position == "goalkeeper":
                sum_goalkeeper += player.ability
            elif player.position == "midfielders":
                sum_midfielders += player.ability
            elif player.position == "forwards":
                sum_forwards += player.ability
            elif player.position == "defenders":
                sum_defenders += player.ability

        return (sum_goalkeeper, sum_defenders, sum_midfielders, sum_forwards)

class Match:
    def __init__(self, home: Team, away: Team, home_goals = 0, aways_goals = 0):
        self.home = home
        self.away = away
        self.home_goals = home_goals
        self.away_goals = aways_goals
    def play_match(self):
        a_home = 0
        d_home = 0
        a_away = 0
        d_away = 0

        for i in range(len(self.home.abilities())):
            if i < 2:
                a_home += self.home.abilities()[i]
            else:
                d_home += self.home.abilities()[i]
        for j in range(len(self.away.abilities())):
            if i < 2:
                a_away += self.away.abilities()[i]
            else:
                d_away += self.away.abilities()[i]

        difference1 = a_home - d_away
        difference2 = a_away - d_home

        if difference1 > 20:
            self.home_goals = random.randint(0,5)
        elif difference1 > 0:
            self.home_goals = random.randint(0,2)

        if difference2 > 20:
            self.away_goals = random.randint(0,5)
        elif difference2 > 0:
            self.away_goals = random.randint(0,2)

    def __str__(self):
        return((self.home.name + str(self.home_goals) + " - " + self.away.name + str(self.away_goals)))

"""
Match:

- two Teams
- goals: 3 points for the winning team, 1 point for each if a tie


"""
