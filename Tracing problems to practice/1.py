# Tracing 1
class QuizA:
    def __init__(self):
        self.x = 6
        self.y = 3
        self.sum = 2
        self.c = 7

    def methodA(self, x):
        self.y = x - self.sum + self.c
        self.c -= 1
        self.sum = x + self.y
        print(self.x, self.y, self.sum)

    def methodB(self, a):
        y = 5
        a.sum = self.x - self.sum
        self.sum = a.x + self.c
        print(self.x, self.c, self.sum)


a = QuizA()
b = QuizA()
a.methodB(b)
b.methodA(b.sum)
b.methodA(a.y)