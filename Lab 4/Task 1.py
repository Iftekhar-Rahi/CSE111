class Customer:
    def __init__(self,name=None):
        self.name=name
    def greet(self,name=None):
        if name==None:
            print("Hello!")
        else:
            print(f"Hello {name}!")
    def purchase(self,*args):

        print(f"{self.name}, you purchased {len(args)} item(s):")
        for i in args:
            print(i)
customer_1 = Customer("Sam")
customer_1.greet()
customer_1.purchase("chips", "chocolate", "orange juice")
print("-----------------------------")
customer_2 = Customer("David")
customer_2.greet("David")
customer_2.purchase("orange juice")