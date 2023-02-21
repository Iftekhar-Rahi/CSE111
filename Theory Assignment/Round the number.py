inp=float(input())
floor=inp//1
ceil=floor+1
middle=(floor+ceil)/2
if inp<middle:
    print(float(floor))
elif inp>=middle:
    print(float(ceil))