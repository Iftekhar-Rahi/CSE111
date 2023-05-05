#String_5
word=input()
low=False
up=False
digit=False
spc=False
sp="_$#!@"
for i in word:
  if i.isupper():
    up=True
  if i.islower():
    low=True
  if i.isdigit():
    digit=True
  if i in sp:
    spc=True
s=""
if low==False:
  s+="Lowercase Missing"
  s+=","
if up==False:
  s+="Uppercase character Missing"
  s+=","
if digit==False:
  s+="Digit Missing"
  s+=","
if spc==False:
  s+="Special Missing"
  s+=","

if s=="":
  print("OK")
else:
    print(s[0:len(s) - 1])