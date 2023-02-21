num=int(input())
s=""
for i in range(num):
    word=input().split(" ")
    w1,w2=word
    if len(w1)>len(w2):
        for i in range(len(w2)):
            s+=w1[i]+w2[i]
        s=s+w1[len(w2): :]
        print(s)
        s=""
    else:
        for i in range(len(w1)):
            s+=(w1[i]+w2[i])
        s=s+w2[len(w1)::]
        print(s)
        s=""