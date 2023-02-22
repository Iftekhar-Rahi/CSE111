#Vjudge_e
test=int(input())
for j in range(test):
  inpt=input().split()
  n,x=[int(i) for i in inpt]
  n=input().split()
  n=[int(i) for i in n]
  # print(n)
  sum=0
  for k in range(x):
    sum+=n[k]
  if sum%2==0:
    print("No")
  else:
    print("Yes")