#Task 4
class Player:
  def __init__(self,name):
    self.name=name
class Team:
  def __init__(self,name=None):
    self.__team=None
    self.__clist=None
    self.setlist([])
    if name==None:
      pass
    else:
      self.setName(name)
  def setName(self,team):
    self.__team=team
  def setlist(self,x):
    self.__clist=x
  def addPlayer(self,location):
    self.getlist().append(location.name)
  def getlist(self):
    return self.__clist
  def getteam(self):
    return self.__team
  def printDetail(self):
    print(f"=====================")
    print(f"Team: {self.getteam()}")
    print("List of Players:")
    print(f"{self.getlist()}")
    print(f"=====================")
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