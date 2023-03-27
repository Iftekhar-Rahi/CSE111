#Task 1
import math
class Circle:
  def __init__(self,r):
    self.__r=r
  def getRadius(self):
    return self.__r
  def area(self):
    area=math.pi*self.getRadius()**2
    return area
  def setRadius(self,x):
    self.__r=x
c1 = Circle(4)
print("First circle radius:" , c1.getRadius())
print("First circle area:" , c1.area())
# c1.setRadius(3)
# print("First circle radius:" , c1.getRadius())
# print("First circle area:" , c1.area())
c2 = Circle(5)
print("Second circle radius:" , c2.getRadius())
print("Second circle area:" , c2.area())