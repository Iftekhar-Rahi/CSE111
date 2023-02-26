class Match:
    def __init__(self,name):
        print("5..4..3..2..1.. Play !!!")
        t=str(name).split('-')
        self.bat=t[0]
        self.ball = t[1]
        self.run=0
        self.wic=0
        self.over=0
    def add_run(self,x):
        self.run += x
    def add_over(self,y):
        if (self.over+y)<=5:
            self.over += y
        elif (self.over+y)>5:
            print(f"Warning! Cannot add {y} over/s (5 over match)")
    def add_wicket(self,z):
        self.wic +=z
    def print_scoreboard(self):
        return f"Batting Team: {self.bat}\nBatting Team: {self.ball}\nTotal Runs: {self.run} Wickets: {self.wic} Overs: {self.over}"
match1 = Match("Rangpur Riders-Cumilla Victorians")
print("=========================")
match1.add_run(4)
match1.add_run(6)
match1.add_over(1)
print(match1.print_scoreboard())
print("=========================")
match1.add_over(5)
print("=========================")
match1.add_wicket(1)
print(match1.print_scoreboard())
