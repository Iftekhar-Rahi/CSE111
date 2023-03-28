def palindrome(w):
    flag_p=None
    flag=None
    s=""
    for i in w:
        if i!=" ":
            s+=i
    y=len(s)
    for i in range(len(s)):
        for j in range(-1,-y-1,-1):
            if i==len(s)//2:
                break
            elif w[i]==w[j]:
                pass
            elif w[i]!=w[j]:
                flag=True
    if flag_p==True:
        print("Palindrome")
    elif flag==True:
        print("Not a palindrome")
palindrome('hello')
