# Task 2
class Triangle:
    def __init__(self, b, h):
        self.__b = 0
        self.setb(b)
        self.__h = h
        self.seth(h)

    def setb(self, b):
        self.__b = b

    def seth(self, h):
        self.__h = h

    def getBase(self):
        return self.__b

    def getHeight(self):
        return self.__h

    def area(self):
        return .5 * self.getBase() * self.getHeight()


t1 = Triangle(10, 5)
print("First Triangle Base:", t1.getBase())
print("First Triangle Height:", t1.getHeight())
print("First Triangle area:", t1.area())

t2 = Triangle(5, 3)
print("Second Triangle Base:", t2.getBase())
print("Second Triangle Height:", t2.getHeight())
print("Second Triangle area:", t2.area())