class BracuStudent:
    def __init__(self,name,home):
        self.name=name
        self.home=home
        self.pas=False

    def show_details(self):
        print(f"Student Name: {self.name}\n"
              f"Lives in {self.home}\n"
              f"Have Bus Pass? {self.pas}")
    def get_pass(self):
        self.pas=True
class BracuBus:
    def __init__(self,location,cap=2):
        self.__cap=cap
        self.__loc=location
        self.__plist=[]
        self.__p_name=[]
    def getCap(self):
        return self.__cap
    def getLoc(self):
        return self.__loc
    def getPlist(self):
        return self.__plist
    def getPname(self):
        return self.__p_name
    def show_details(self):
        print(f"Bus Route: {self.getLoc()}\n"
              f"Passengers Count: {len(self.getPlist())} (Max: {self.getCap()})\n"
              f"Passengers On Board: {self.getPname()}")
    def board(self,*args):
        if len(args) == 0:
            print("No passenger!")
        else:
            for j in args:
                if len(self.getPlist()) == self.getCap():
                    print(f"Bus is full!!")
                elif j.pas == False:
                    print("You don't have bus pass!")
                elif self.getLoc() != j.home:
                    print("You got on wrong bus!")
                else:
                    self.getPlist().append(j)
                    self.getPname().append(j.name)
                    print(f"{j.name} boarded the bus")



st1 = BracuStudent("Afif", "Mirpur")
print("1===========================")
st2 = BracuStudent("Shanto", "Motijheel")
st3 = BracuStudent("Taskin", "Mirpur")
st1.show_details()
st2.show_details()
print("2===========================")
st3.show_details()
print("3===========================")
bus1 = BracuBus("Mirpur")
bus2 = BracuBus("Azimpur", 5)
bus1.show_details()
bus2.show_details()
print("4===========================")
st2.get_pass()
st3.get_pass()
print("5===========================")
st2.show_details()
st3.show_details()
print("6===========================")
bus1.board()
print("7===========================")
bus1.board(st1, st2)
print("8===========================")
st1.get_pass()
st2.home = "Mirpur"
st1.show_details()
st2.show_details()
print("9===========================")
bus1.board(st1, st2, st3)
print("10===========================")
bus1.show_details()
