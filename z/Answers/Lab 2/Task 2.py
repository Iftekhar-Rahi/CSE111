def rahi(h,w):
    h = h / 100
    bmi=w/(h*h)
    print(f"Score is {round(bmi,1)}.", end=" ")
    if bmi > 30:
        print("You are Obese")
    elif bmi >=25 and bmi <= 30:
        print("You are overweight")
    elif bmi >= 18.5 and bmi <= 24.9:
        print("You are Noramal")
    elif bmi < 18.5:
        print("You are underweight")
    return
rahi(152,48)