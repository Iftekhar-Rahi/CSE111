#Task 6
class Shape:

  def __init__(self, name='Default', height=0, base=0):
    self.area = 0
    self.name = name
    self.height = height
    self.base = base

  def get_height_base(self):
    return "Height: "+str(self.height)+",Base: "+str(self.base)

#write your code here
class triangle(Shape):
  def calcArea(self):
    self.area=.5*self.base*self.height
  def printDetail(self):
    s=f"Shape name: {self.name}\n"
    s+=super().get_height_base()
    s+=f"\nArea: {self.area}"
    return s
class trapezoid(Shape):
  def __init__(self,name,height,base,side):
    super().__init__(name,height,base)
    self.side=side
  def calcArea(self):
    self.area=(.5*(self.base+self.side))*self.height
  def printDetail(self):
    s=f"Shape name: {self.name}\n"
    s+=f"{super().get_height_base()}, Side_A: {self.side}\n"
    s+=f"Area: {self.area}"
    return s
tri_default = triangle()
tri_default.calcArea()
print(tri_default.printDetail())
print('--------------------------')
tri = triangle('Triangle', 10, 5)
tri.calcArea()
print(tri.printDetail())
print('---------------------------')
trap = trapezoid('Trapezoid', 10, 6, 4)
trap.calcArea()
print(trap.printDetail())
