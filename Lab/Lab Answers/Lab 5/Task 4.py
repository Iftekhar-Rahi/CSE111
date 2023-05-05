class Player:
    def __init__(self,name):
        self.name=name
class Team:
    def __init__(self,name="Bangladesh"):
        self.__t_name=name
        self.__plist=[]
    def getTname(self):
        return self.__t_name
    def getPlist(self):
        return self.__plist
    def setName(self,x):
        self.__t_name = x
    def printDetail(self):
        print("=====================")
        print(f"Team: {self.getTname()}")
        print("List of Players:")
        print(f"{self.getPlist()}")
    def addPlayer(self,*location):
        for i in location:
            self.getPlist().append(i.name)


b = Team()
b.setName('Bangladesh')
mashrafi = Player("Mashrafi")
b.addPlayer(mashrafi)
tamim = Player("Tamim")
b.addPlayer(tamim)
b.printDetail()
a = Team("Australia")
ponting = Player("Ponting")
a.addPlayer(ponting)
lee = Player("Lee")
a.addPlayer(lee)
a.printDetail()
