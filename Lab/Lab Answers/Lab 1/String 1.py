#String_1
word=input()
up=0
low=0
for i in word:
  if i.isupper():
    up+=1
  else:
    low+=1
if up>low:
  print(word.upper())
else:
  print(word.lower())