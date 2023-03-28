#String_4
w1,w2=input().split(",")
s=""
for i in w1:
    if i in w2:
        s += i
for i in w2:
    if i in w1:
        s+= i
if len(s)==0:
  print("Nothing in common. ")
else:
  print(s)