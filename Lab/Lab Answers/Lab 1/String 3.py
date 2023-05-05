#String_3
word=input()
start=None
end=None
for i in range (0,len(word)):
  if word[i].isupper():
    if start==None:
      start=i
      # print(start)
    else:
      end=i
      # print(end)
word_s=word[start+1:end]

if len(word_s)==0:
  print("BLANK")
else:
    print(word_s)