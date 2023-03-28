#List_1
my_list=[]
uni_list=[]
while True:
  word=input()
  if word.upper()!="STOP":
    my_list.append(int(word))
  else:
    break
for i in my_list:
  if i not in uni_list:
    uni_list.append(i)
for i in uni_list:
  print(f"{i} - {my_list.count(i) } times")