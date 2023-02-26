class Batsman:
    def __init__(self,*args):
        if len(args)==3:
            self.name = args[0]
            self.run = args[1]
            self.ball = args[2]
        elif len(args)!=3:
            self.name = "New Batsman"
            self.run = args[0]
            self.ball = args[1]
        self.rate=0
    def printCareerStatistics(self):
        print(f"Name: {self.name}")
        print(f"Runs Scored: {self.run} , Balls Faced: {self.ball}")
    def battingStrikeRate(self):
        self.rate=(self.run / self.ball) * 100
        return self.rate
    def setName(self,x):
        self.name=x
b1 = Batsman(6101, 7380)
b1.printCareerStatistics()
print("============================")
b2 = Batsman("Liton Das", 678, 773)
b2.printCareerStatistics()
print("----------------------------")
print(b2.battingStrikeRate())
print("============================")
b1.setName("Shakib Al Hasan")
b1.printCareerStatistics()
print("----------------------------")
print(b1.battingStrikeRate())