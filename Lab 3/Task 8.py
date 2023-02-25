class Calculator:
    def __init__(self):
        print("Let’s Calculate!")
        self.first_value = 0
        self.second_value = 0
        self.operator = None
        self.rahi = 0
    def add(self):
        print(f"Result: {self.first_value+self.second_value}")
    def substract(self):
        print(f"Result: {self.first_value - self.second_value}")
    def multiply(self):
        print(f"Result: {self.first_value * self.second_value}")
    def divide(self):
        print(f"Result: {self.first_value / self.second_value}")
obj=Calculator()
obj.first_value=int(input("Value 1: "))
obj.operator=input("Operator: ")
obj.second_value=int(input("Value 2: "))
# print(f"Value 1: {obj.first_value}")
# print(f"Value 1: {obj.operator}")
# print(f"Value 2: {obj.second_value}")
if obj.operator == "+":
    obj.add()
elif obj.operator == "-":
    obj.substract()
elif obj.operator == "*":
    obj.multiply()
elif obj.operator == "/":
    obj.divide()