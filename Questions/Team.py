class CricketMatch:
    def __init__(self,match,over,team1,team2):
      self.match=match
      self.team1=team1
      self.team2=team2
      self.over=over

    def showScoreCard(self):
      print(f"Match name:{self.match}")
      print(f"{self.team1.name} vs {self.team2.name}")

class Team:
    def __init__(self, name):
        self.name = name
        self.pList = []  # To store player list.
        self.score = 0  # Runs scored by the team
        self.wicketLeft = 0  # How many wickets left?
        self.nextBatsman = 2  # Next batsman/player index

    # Write addPlayers method here.
    def addPlayers(self, *args):
        for i in args:
            self.pList.append(i)


    # Write printSquad method here
    def printSquad(self):
        print(f"Team name:{self.name}")
        print("List of Players:")
        s = ""
        for i in self.pList:
            s += f"{i.name}({i.jn}),"
        s = s[:-1:]
        print(s)


class Player:
    def __init__(self, name, jersey_number):
        self.name = name
        self.jn = jersey_number


p1 = Player("Alice", 9)
p2 = Player("Bob", 3)
p3 = Player("Robin", 6)
p4 = Player("Carol", 14)
p5 = Player("Jeck", 12)
p6 = Player("Ethan", 2)
p7 = Player("John", 35)
p8 = Player("Jackson", 7)
p9 = Player("Aiden", 17)
p10 = Player("Jameson", 11)
p11 = Player("Wyatt", 87)
p12 = Player("Jackson", 1)
print("1------------------")
t1 = Team("Rangpur Rangers")
t2 = Team("Barishal Bulls")
print("2------------------")
t1.addPlayers(p1, p3, p4)
t1.addPlayers(p7, p8)
t1.addPlayers(p11)
print("3------------------")
t2.addPlayers(p2, p5)
t2.addPlayers(p6)
t2.addPlayers(p9, p10, p12)
print("4------------------")
t1.printSquad()
print("5------------------")
t2.printSquad()
print("6------------------")
cm1 = CricketMatch("Fast5", 5, t1, t2)
cm1.showScoreCard()
print("7------------------")
cm1.updateScoreCard(["WB", 2, 1, 4, "W", 6, 3])
print("8------------------")
cm1.showScoreCard()
print("9------------------")
cm1.updateScoreCard(["W", 1, 1, "NB", "W", 1, 1])
print("10------------------")
cm1.showScoreCard()
print("11------------------")
cm1.updateScoreCard(["W", 6, 6, 6, "W"])
print("12------------------")
cm1.showScoreCard()