#list 3
list1=input().split()
list1=[int (i) for i in list1]
list2=input().split()
list2=[int (i) for i in list2]
new=[]
for i in list1:
  for j in list2:
    new.append(j*i)
print(new)