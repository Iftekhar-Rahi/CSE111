def add_divisor(min,max,div):
    s=0
    for i in range(min,max):
        if i%div==0:
            s+=i
    return s
print(add_divisor(3,16,3))