class PizzaMachine:
    def __init__(self,name="Regular",size=6):
        self.name=name
        self.size=size
        self.topping=None
        self.spicelevel=None
    def customizePizza(self,topping,spicelevel="Regular"):
        self.topping=topping
        self.spicelevel=spicelevel
        if type(self.topping)==str:
            return f"No toppings specified! Can't bake pizza."
        elif spicelevel not in ["Regular","Hot","Super Naga"]:
            return f"Sorry! Spice level not allowed. Can't bake pizza."
        else:
            return f"Your {self.size}-inch {self.spicelevel} spicy {self.name} Pizza is ready with {','.join(topping)} toppings. Enjoy!"
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