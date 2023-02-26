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
                    if ord(data[j][0][0]) > ord(data[j + 1][0][0]):
                        data[j + 1], data[j] = data[j], data[j + 1]
                        break
for i in data:
    print(' '.join(i))
