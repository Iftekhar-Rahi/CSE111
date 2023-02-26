#no 1 (solved)
n=int(input())
data=[]
for i in range(n):
  data.append(input().split())
for i in range(n):
    for j in range(0, n-i-1):
        if int(data[j][1])<int(data[j+1][1]):
            data[j + 1], data[j] = data[j], data[j + 1]
        elif int(data[j][1])==int(data[j+1][1]):
            if int(data[j][2])<int(data[j+1][2]):
                data[j + 1],data[j]=data[j],data[j+1]
            elif int(data[j][2])==int(data[j+1][2]):
                if int(data[j][3])<int(data[j+1][3]):
                    data[j + 1], data[j] = data[j], data[j + 1]
                elif int(data[j][3])==int(data[j+1][3]):
                    for i in range(len(data[j][0])-1):
                        if ord(data[j][0][i])>ord(data[j+1][0][i]):
                            data[j + 1], data[j] = data[j], data[j + 1]
                            break
for i in data:
    print(' '.join(i))