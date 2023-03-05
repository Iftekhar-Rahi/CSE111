class MidA:
    def __init__(self):
        self.x = 3
        self.y = 7
        self.sum = 0
    def methodA(self, x):
        self.y = x + self.sum + self.x
        self.sum = x + self.y
        z = MidA()
        z.sum = self.sum + self.y
        self.methodB(z)
        print(self.x, self.y, self.sum)
    def methodB(self, a):
        y = 3
        a.x = self.x + self.sum;
        self.sum = a.x + a.y + y
        print(a.x, a.y, a.sum)
a=MidA()
a.methodA(5)