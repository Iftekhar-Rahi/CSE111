num=int(input())
mylist=[]
even=[]
odd=[]
for i in range(num):
    nums=int(input())
    mylist.append(nums)
for i in mylist:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
odd.sort(reverse=True)
even.sort()
for i in even:
    print(i)
for i in odd:
    print(i)