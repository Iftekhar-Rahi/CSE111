class Programmer:
    def __init__(self,name,lng,ex):
        self.name=name
        self.lng=lng
        self.ex=ex
        print("Horray! A new programmer is born")
    def printDetails(self):
        print(f"Name: {self.name}")
        print(f"Language: {self.lng}")
        print(f"Experience: {self.ex} years.")
    def addExp(self,x):
        print(f"Updating experience of {self.name}")
        self.ex += x
p1 = Programmer("Ethen Hunt", "Java", 10)
p1.printDetails()
print('--------------------------')
p2 = Programmer("James Bond", "C++", 7)
p2.printDetails()
print('--------------------------')
p3 = Programmer("Jon Snow", "Python", 4)
p3.printDetails()
p3.addExp(5)
p3.printDetails()