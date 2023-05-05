#Task 3
class Tournament:
    def __init__(self,name='Default'):
        self.__name = name
    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name

#write your code here
class Cricket_Tournament(Tournament):
    def __init__(self,name="Default",team=0,typ="No type"):
      super().__init__(name)
      # super().set_name(name)
      self.team=team
      self.typ=typ
    def detail(self):
      s=f"Cricket Tournament Name: {super().get_name()}\n"
      s+=f"Number of Teams: {self.team}\n"
      s+=f"Type: {self.typ}"
      return s
class Tennis_Tournament(Tournament):
    def __init__(self,name,player):
      super().__init__(name)
      # super().set_name(name)
      self.player=player
    def detail(self):
      s=f"Tennis Tournament Name: {super().get_name()}\n"
      s+=f"Number of Players: {self.player}"
      return s
ct1 = Cricket_Tournament()
print(ct1.detail())
print("-----------------------")
ct2 = Cricket_Tournament("IPL",10,"t20")
print(ct2.detail())
print("-----------------------")
tt = Tennis_Tournament("Roland Garros",128)
print(tt.detail())
