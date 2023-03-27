# Task 6
class Train:
    def __init__(self, train, *args):
        self.__train = train
        self.__start = args[0]
        self.__end = args[-1]
        self.list = []
        self__stations = args
        self.__fair = 0
        print(f"Welcome aboard on {self.getTrain()}\n"f"Start: {self.getStart()}\n"f"Destination: {self.getEnd()}")

    def getTrain(self):
        return self.__train

    def getStart(self):
        return self.__start

    def getEnd(self):
        return self.__end

    def getFair(self):
        return self.__fair

    def getStations(self):
        return self.__stations

    def setFair(self, x):
        self.__fair = x

    def addPassenger(self, *args):
        for location in args:
            print(f"{location.name} welcome aboard")
            self.list.append(location)

    def allPassengerDetails(self):
        for i in self.list:
            f = ((self.getStations().index(i.end)) - (self.getStations().index(i.start))) * 100
            self.setFair(f)
            print(f"Name: {i.name}\n"f"Start: {i.start}\n"f"Destination: {i.end}\n")
            "f"
            Fair: {self.getFair()}\n
class Passenger:
    def __init__(self, name, start="New York", end="Boston"):
        self.name = name
        self.start = start
        self.end = end
        # print(f"{self.name} welcome aboard")


t1 = Train('T1-Express', 'New York', 'Manhattan', 'Brooklyn', 'Boston')
print("1========================")
p1 = Passenger("Naruto")
t1.addPassenger(p1)
p2 = Passenger("Sasuke", "Manhattan")
p3 = Passenger("Hinata", "Manhattan", "Brooklyn")
print("2========================")
t1.addPassenger(p2, p3)
print("3========================")
t1.allPassengerDetails()
print("4========================")
t2 = Train('Europe-Express', 'London', 'Paris', 'Brussels', 'Turkey')
print("5========================")
p4 = Passenger("Max", "London", "Brussels")
p5 = Passenger("Eleven", "Paris")
p6 = Passenger("Mike", "Brussels")
t2.addPassenger(p4, p5, p6)
print("6========================")
t2.allPassengerDetails()
