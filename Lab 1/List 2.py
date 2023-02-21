#List_2
num=int(input())
sumation=[]
lol=[]
for i in range(num):
  mylist=input().split(" ")
  final_list=[int (i) for i in mylist]
  sumation.append(sum(final_list))
  lol.append(final_list)
print(max(sumation))
print(lol[sumation.index(max(sumation))])