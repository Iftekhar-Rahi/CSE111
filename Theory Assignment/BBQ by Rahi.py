while True:
    try:
        num=int(input())
        dic = {}
        number=[]
        for i in range(num):
            w1,w2 = input().split(" ")
            dic[int(w2)] = w1
            number.append(int(w2))
        number.sort()
        for j in number:
            for k, v in dic.items():
                if j == k:
                    if number[-1] != j:
                        print(v, end=" ")
                    else:
                        print(v)
    except:
        break