def cart(name,location="MOHAKHALI"):
    dict={"BBQ Chicken Cheese Burger":250,"Beef Burger":170,"Naga Drums":200}
    s=0
    for k,v in dict.items():
        if k==name:
            s+=v
            s+=s*(.08)
            # print(s)
            if location.upper() != "MOHAKHALI":
                s += 60
            else:
                s += 40
        # print(s)
    return s
print(cart("Beef Burger","rahi"))