#Task 12
class Calculator:
    def __init__(self):
        print("Calculator is ready!")
        self.x=0
        self.y = 0
        self.oppa=None
        self.rahi=0
    def calculate(self,x,y,oppa):
        self.x = x
        self.y = y
        self.oppa = oppa
        if oppa=="+":
            self.rahi=self.x+self.y
            return self.rahi
        elif oppa=="-":
            self.rahi=self.x-self.y
            return self.rahi
        elif oppa=="*":
            self.rahi=self.x*self.y
            return self.rahi
        elif oppa=="/":
            self.rahi=self.x/self.y
            return self.rahi
    def showCalculation(self):
        if self.oppa=="+":
            print(f"{self.x}+{self.y}={self.rahi}")
        elif self.oppa=="-":
            print(f"{self.x}-{self.y}={self.rahi}")
        elif self.oppa=="*":
            print(f"{self.x}*{self.y}={self.rahi}")
        elif self.oppa=="/":
            print(f"{self.x}/{self.y}={self.rahi}")
c1 = Calculator()
print("==================")
val = c1.calculate(10, 20, '+')
print("Returned value:", val)
c1.showCalculation()
print("==================")
val = c1.calculate(val, 10, '-')
print("Returned value:", val)
c1.showCalculation()
print("==================")
val = c1.calculate(val, 5, '*')
print("Returned value:", val)
c1.showCalculation()
print("==================")
val = c1.calculate(val, 16, '/')
print("Returned value:", val)
c1.showCalculation()