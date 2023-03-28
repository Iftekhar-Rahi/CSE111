#list 4
while True:
  num=input()
  ub=None
  if num.upper()=="STOP":
    break
  else:
    mylist=num.split()
    givenlist=[]
    result=[]
    for i in mylist:
      givenlist.append(int(i))
    for i in range (len(givenlist)-1):
      sub=abs(givenlist[i]-givenlist[i+1])
      result.append(sub)
    for i in range(max(result)):
      if i in result:
        ub=True
      else:
        ub=False
    if ub==True:
      print("UB Jumper")
    else:
      print("Not UB Jumper")