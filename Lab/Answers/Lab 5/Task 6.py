class Passenger:
    def __init__(self,p_name,start=None,end=None):
        self.p_name=p_name
        self.start=start
        self.end=end

class Train:
    def __init__(self,t_name,*stations):
        self.t_name=t_name
        self.start=stations[0]
        self.end=stations[-1]
        self.lplist = []
        self.stations=stations
        print(f"Welcome aboard on {self.t_name}")
        print(f"Start: {self.start}")
        print(f"Destionation: {self.end}")
    def addPassenger(self,*location):
        for i in location:
            self.lplist.append(i)
            print(f"{i.p_name} welcome aboard")
    def allPassengerDetails(self):
        for location in self.lplist:
            if location.start==None:
                location.start=self.start
            if location.end==None:
                location.end=self.end
            print(f"Name: {location.p_name}",end=",")
            print(f"Start: {location.start}",end = ",")
            print(f"Destination: {location.end}", end=",")
            print((f"Fair: ${(self.stations.index(location.end)-self.stations.index(location.start))*100}"))




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

