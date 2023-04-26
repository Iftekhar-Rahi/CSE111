#Task 7
class SportsPerson:

  def __init__(self, team_name, name, role):
    self.__team = team_name
    self.__name = name
    self.role = role
    self.earning_per_match = 0

  def get_name_team(self):
    return 'Name: '+self.__name+', Team Name: ' +self.__team

#write your code here
class Player(SportsPerson):
  def __init__(self,team_name, name, role,goal,matchs):
    super().__init__(team_name, name, role)
    self.goal=goal
    self.matchs=matchs
    self.ratio=0
    self.earning_per_match=(self.goal * 1000) + (self.matchs * 10)
  def calculate_ratio(self):
    self.ratio=self.goal/self.matchs
  def print_details(self):
    print(super().get_name_team())
    s=f"Team Role: {self.role}\nTotal Goal: {self.goal}, Total Played: {self.matchs}\nGoal Ratio: {self.ratio}\nMatch Earning: {self.earning_per_match}K"
    print(s)
class Manager(SportsPerson):
  def __init__(self,team_name, name, role,win):
    super().__init__(team_name, name, role)
    self.win=win
    self.earning_per_match=self.win*1000
  def print_details(self):
    print(super().get_name_team())
    print(f"Team Role: {self.role}\nTotal Win: {self.win}\nMatch Earning: {self.earning_per_match}K")
player_one = Player('Juventus', 'Ronaldo', 'Striker', 25, 32)
player_one.calculate_ratio()
player_one.print_details()
print('------------------------------------------')
manager_one = Manager('Real Madrid', 'Zidane', 'Manager', 25)
manager_one.print_details()
