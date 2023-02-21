#list 5
count=0
word=input().split(" ")
# def intconverter(rahi):
#   ylist=[]
#   for i in rahi:
#     ylist.append(int(i))
#     return tuple(ylist)

total,times=[int(i) for i in word]
# total,times=intconverter(word)
tries=input().split(" ")
# mylist=intconverter(tries)
mylist=[int (i) for i in tries]
for i in mylist:
  if (i+times)<=5:
    count+=1
print(count//3)