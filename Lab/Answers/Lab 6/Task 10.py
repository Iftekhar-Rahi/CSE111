class SultansDine:
  total_branch = 0
  total_sell = 0
  branch_list = []
  def __init__(self, location):
    self.loc = location
    SultansDine.total_branch += 1
  def sellQuantity(self, quantity):
    if quantity < 10:
      self.branch_sell = quantity * 300
    elif quantity < 20:
      self.branch_sell = quantity * 350
    else:
      self.branch_sell = quantity * 400
    SultansDine.total_sell += self.branch_sell
    self.sell_per = (self.branch_sell / SultansDine.total_sell) * 100
    self.sell_per = round(self.sell_per, 2)
    SultansDine.branch_list.append(f"Branch Name: {self.loc}, Branch Sell: {self.branch_sell} Taka\nBranch consists of total sell's: {self.sell_per}%")
  def branchInformation(self):
    print("Branch name:", self.loc)
    print("Branch Sell:", self.branch_sell, "Taka")
  @classmethod
  def details(cls):
    print("Total Number of branch(s):", cls.total_branch)
    print("Total Sell:", cls.total_sell, "Taka")
    for i in cls.branch_list:
      print(i)
SultansDine.details()
print('########################')
dhanmondi = SultansDine('Dhanmondi')
dhanmondi.sellQuantity(25)
dhanmondi.branchInformation()
print('-----------------------------------------')
SultansDine.details()
print('========================')
baily_road = SultansDine('Baily Road')
baily_road.sellQuantity(15)
baily_road.branchInformation()
print('-----------------------------------------')
SultansDine.details()
print('========================')
gulshan = SultansDine('Gulshan')
gulshan.sellQuantity(9)
gulshan.branchInformation()
print('-----------------------------------------')
SultansDine.details()