class Match:
    def __init__(self,*name):
        print("5..4..3..2..1.. Play !!!")
        t=name.split('-')
        self.bat=t[0]
        self.ball = t[1]
        self.run=0
        self.wic=0
        self.over=0
    def add_run(self,x):
        self.run += x
    def add_over(self,y):
        self.over+=y
    def add_wicket(self,z):
        self.wic +=z
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
