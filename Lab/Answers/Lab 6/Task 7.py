#Task 7
class Cat:
  Number_of_cats=0
  def __init__(self,color,situation):
    self.color=color
    self.situation=situation
    Cat.Number_of_cats+=1
  @classmethod
  def no_parameter(cls):
    obj=cls("White","sitting")
    return obj
  @classmethod
  def first_parameter(cls,color):
    obj=cls(color,"sitting")
    return obj
  @classmethod
  def second_parameter(cls,position):
    obj=cls("Grey",position)
    return obj
  def printCat(self):
    print(f"{self.color} cat is {self.situation}")
  def changeColor(self,c):
    self.color=c
print("Total number of cats:", Cat.Number_of_cats)
c1 = Cat.no_parameter()
c2 = Cat.first_parameter("Black")
c3 = Cat("Brown", "jumping")
c4 = Cat("Red", "purring")
c5 = Cat.second_parameter("playing")
print("=======================")
c1.printCat()
c2.printCat()
c3.printCat()
c4.printCat()
c5.printCat()
c1.changeColor("Blue")
c3.changeColor("Purple")
c1.printCat()
c3.printCat()
print("=======================")
print("Total number of cats:", Cat.Number_of_cats)
