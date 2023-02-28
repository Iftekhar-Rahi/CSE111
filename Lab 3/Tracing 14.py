class Test:
    def __init__(self):
        self.sum = 0
        self.y = 0

    def methodA(self):
        x=0
        y=0
        y = y + 7
        x = y + 11
        self.sum = x + y
        print(x , y, self.sum)

    def methodB(self):
        x = 0
        self.y = self.y + 11
        x = x + 33 + self.y
        self.sum = self.sum + x + self.y
        print(x , self.y, self.sum)

t1=Test()
t1.methodA()
t1.methodA()
t1.methodB()
t1.methodB()