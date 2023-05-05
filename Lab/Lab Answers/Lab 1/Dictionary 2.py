#Dictionary_2
mylist = []
dic = {}
while True:
    num = input()
    if num.upper() == "STOP":
        break
    else:
        mylist.append(int(num))
    for i in mylist:
        dic[i] = mylist.count(i)
print(dic)
for i in dic:
    print(f"{i}-{dic[i]} times")