class Shape:
    def __init__(self,shape,a,b):
        self.shape=shape
        self.a=a
        self.b=b
        # self.area=0
    def area(self):
        if self.shape.upper()=="TRIANGLE" or self.shape.upper()=="RHOMBUS":
            self.area=.5*self.a*self.b
            print(f"Area: {float(self.area)}")
        elif self.shape.upper()=="RECTANGLE" or self.shape.upper()=="SQUARE":
            self.area = self.a * self.b
            print(f"Area: {float(self.area)}")
        else:
            print("Area: Shape unknown ")
triangle = Shape("Triangle",10,25)
triangle.area()
print("==========================")
square = Shape("Square",10,10)
square.area()
print("==========================")
rhombus = Shape("Rhombus",18,25)
rhombus.area()
print("==========================")
rectangle = Shape("Rectangle",15,30)
rectangle.area()
print("==========================")
trapezium = Shape("Trapezium",15,30)
trapezium.area()
