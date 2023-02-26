num=int(input())
for i in range(num):
    mylist = []
    s = ""
    word=input()
    for i in word:
        mylist.append(int(i))
        mylist.sort()
        zero=mylist.count(0)
    for i in mylist:
        if i!=0:
            s+=str(i)
    s=s[0]+"0"*zero+s[1:]
    print(int(s))