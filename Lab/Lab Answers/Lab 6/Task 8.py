#Task 8
import math
class Cylinder:
  radius=5
  height=18
  def __init__(self,r,h):
    self.radius=r
    self.height=h
    print(f"Default radius={Cylinder.radius} and height={Cylinder.height}.")
    print(f"Updated: radius={self.radius} and height={self.height}.")
    Cylinder.radius=self.radius
    Cylinder.height=self.height
  @staticmethod
  def area(r,h):
    ans=(2*math.pi*r**2)+(2*math.pi*r*h)
    print(ans)
  @staticmethod
  def volume(r,h):
    ans=math.pi*h*r**2
    print(ans)
  @classmethod
  def swap(cls,h,r):
    obj=cls(r,h)
    return obj
  @classmethod
  def changeFormat(cls,z):
    data=z.split("-")
    obj=cls(float(data[0]),float(data[1]))
    return obj

c1 = Cylinder(0,0)
Cylinder.area(c1.radius,c1.height)
Cylinder.volume(c1.radius,c1.height)
print("===============================")
c2 = Cylinder.swap(8,3)
c2.area(c2.radius,c2.height)
c2.volume(c2.radius,c2.height)
print("===============================")
c3 = Cylinder.changeFormat("7-13")
c3.area(c3.radius,c3.height)
c3.volume(c3.radius,c3.height)
print("===============================")
Cylinder(0.3,5.56).area(Cylinder.radius,Cylinder.height)
print("===============================")
Cylinder(3,5).volume(Cylinder.radius,Cylinder.height)
