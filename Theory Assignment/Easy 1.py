num=int(input())
s=""
for i in range (num):
    word=input().split(" ")
    words=sorted(word,key=len,reverse=True)
    for i in words:
        s+=i+" "
    s=s[0:len(s)-1]
    print(s)
    s=""