#Task 3
class Passenger:
  count=0
  def __init__(self,name):
    self.name=name
    Passenger.count+=1
    self.fair=450
  def set_bag_weight(self,kg):
    if kg<=20:
      pass
    elif 20<kg<=50:
      self.fair+=50
    else:
      self.fair+=100
  def printDetail(self):
    print(f"Name: {self.name}")
    print(f"Bus Fare: {self.fair} taka")
print("Total Passenger:", Passenger.count)
p1 = Passenger("Jack")
p1.set_bag_weight(90)
p2 = Passenger("Carol")
p2.set_bag_weight(10)
p3 = Passenger("Mike")
p3.set_bag_weight(25)
print("=========================")
p1.printDetail()
print("=========================")
p2.printDetail()
print("=========================")
p3.printDetail()
print("=========================")
print("Total Passenger:", Passenger.count)