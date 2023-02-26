while True:
    try:
        word=input()
        s=""
        flag=True
        for i in range(len(word)):
            if word[i]==" ":
                s+=" "
            elif flag==True:
                s+=word[i].upper()
                flag=False
            elif flag==False:
                s+=word[i].lower()
                flag=True
        print(s)
    except:
        break