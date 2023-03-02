# class PizzaMachine:
#     def __init__(self,*args):
#         if len(args)==2:
#             self.name=args[0]
#             self.level=None
#             self.inch=args[1]
#         elif len(args)==1:
#             self.name = args[0]
#             self.level = None
#             self.inch = 6
#         elif len(args)==0:
#             self.name = "Regular"
#             self.level = "Hot"
#             self.inch = 6
#         self.all=["Regular","Hot","Super Naga"]
#     def customizePizza(self,*args):
#         if len(args)==2:
#             self.toppings = args[0]
#             self.level = args[1]
#         elif len(args)==1:
#             self.toppings = args[0]
#         if type(self.toppings)!=list:
#             return f"No toppings specified! Can't bake pizza."
#         else:
#             s=",".join(self.toppings)
#             if self.level in self.all:
#                 if len(self.toppings) == 0:
#                     return f"No toppings specified! Can't bake pizza."
#                 elif len(self.toppings) != 0:
#                     return f"Your {self.inch}-inch {self.level} spicy {self.name} Pizza is ready with {s}. Enjoy!"
#             else:
#                 return f"Sorry! Spice level not allowed. Can't bake pizza."
class PizzaMachine:
    def __init__(self,name="Regular",size=6):
        self.name=name
        self.size=size
    def customizePizza(self,topping,spicelevel="Regular"):
        if type(topping)==str:
            return f"No toppings specified! Can't bake pizza."
        elif spicelevel not in ["Hot","Regular","Super Naga"]:
            return f"Sorry! Spice level not allowed. Can't bake pizza."
        else:
            return f"Your {self.size}-inch {spicelevel} spicy {self.name} Pizza is ready with {','.join(topping)} toppings. Enjoy!"
pizza1 = PizzaMachine()
order1 = pizza1.customizePizza(["Cheese", "Pepperoni"],
"Hot")
print("1################################# ")
print(order1)
print("2================================")
pizza2 = PizzaMachine("Vege")
order2 = pizza2.customizePizza("Super Naga")
print("3#################################")
print(order2)
print("4================================")
pizza3 = PizzaMachine("Chicken Blast",12)
order3 = pizza3.customizePizza(["Mushroom"])
print("5#################################")
print(order3)
print("6================================")
pizza4 = PizzaMachine("Beef Bonanza",16)
order4 = pizza4.customizePizza(["Cheese","Beef kala bhuna"],"Mild")
print("7#################################")
print(order4)
print("8================================")