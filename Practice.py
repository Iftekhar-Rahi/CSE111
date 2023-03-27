class Train:
    def __init__(self,train,*args):
        self.train=train
        self.start=args[0]
        self.destination=args[-1]
        self.plocation=[]
        self.stations=args
        print(f"Welcome aboard on {self.train}\n"
        f"Start: {self.start}\n"
        f"Destination: {self.destination}")
    def addPassenger(self,*location):
        for i in location:
            self.plocation.append(i)
            print(f"{i.p_name} welcome aboard")
    def allPassengerDetails(self):
        for i in self.plocation:
            print(f"Name: {i.p_name},"
            f"Start: {i.start},"
            f"Destination: {i.destination},"
            f"Fair: ${(self.stations.index(i.destination)-self.stations.index(i.start))*100}")
class Passenger:
    def __init__(self,name,start="New York",destination="Boston"):
        self.p_name=name
        self.start=start
        self.destination=destination


t1 = Train('T1-Express','New York','Manhattan','Brooklyn','Boston')
print("1========================")
p1 =Passenger("Naruto")
t1.addPassenger(p1)
p2 = Passenger("Sasuke","Manhattan")
p3 = Passenger("Hinata","Manhattan","Brooklyn")
print("2========================")
t1.addPassenger(p2,p3)
print("3========================")
t1.allPassengerDetails()
print("4========================")
t2 = Train('Europe-Express','London','Paris','Brussels','Turkey')
print("5========================")
p4 =Passenger("Max","London","Brussels")
p5 = Passenger("Eleven","Paris")
p6 = Passenger("Mike","Brussels")
t2.addPassenger(p4,p5,p6)
print("6========================")
t2.allPassengerDetails()
