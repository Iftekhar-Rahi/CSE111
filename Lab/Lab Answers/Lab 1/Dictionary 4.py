#dictionary_4
dic= {1:'.,?!:',2:'ABC',3:'DEF',4:'GHI',5:'JKL',6:'MNO',7:'PQRS',8:'TUV',9:'WXYZ',10:' '}
inp=input().upper()
s=""
for i in inp:
    for k,v in dic.items():
        if i in v:
            # position=v.index(i)+1
            # print(str(k)*position, end="")
            position=v.index(i)+1
            s+=position*str(k)
print(s)