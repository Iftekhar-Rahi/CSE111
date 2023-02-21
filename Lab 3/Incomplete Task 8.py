class Calculator:
    def __init__(self,value1,value2,operator):
        print("Let's Calculate!")
        self.value1=value1
        self.value2=value2
        self.operator=operator
    def add(self):
        if self.operator=="+":
            self.result=self.value1+self.value2
            print(self.result)
    def subtract(self):
        if self.operator=="-":
            self.result=self.value1-self.value2
            print(self.result)
    def multiply(self):
        if self.operator=="*":
            self.result=self.value1*self.value2
            print(self.result)
    def divide(self):
        if self.operator == "/":
            self.result = self.value1 / self.value2
            print(self.result)
b1=Calculator(1,"+",1)