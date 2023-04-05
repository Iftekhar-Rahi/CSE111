class Assassin:
    classVar = 0

    def __init__(self, name, success_rate):
        self.name = name
        self.s_r = success_rate
        Assassin.classVar += 1

    def printDetails(self):
        print(f"Name: {self.name}")
        print(f"Success rate: {self.s_r}%")
        print(f"Total number of Assassin: {Assassin.classVar}")

    @classmethod
    def failureRate(cls, name, failuare_rate):
        obj = cls(name, (100 - failuare_rate))
        return obj

    @classmethod
    def failurePercentage(cls, name, p):
        p=p[:-1]
        obj=cls(name,(100-int(p)))
        return obj
john_wick = Assassin('John Wick', 100)
john_wick.printDetails()
print('================================')
nagisa = Assassin.failureRate("Nagisa", 20)
nagisa.printDetails()
print('================================')
akabane = Assassin.failurePercentage("Akabane", "10%")
akabane.printDetails()
