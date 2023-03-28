def palindrome(w):
    s=""
    for i in w:
        if i!=" ":
            s+=i
    r=len(s)//2
    n1=s[0:r]
    n2=s[-1:-r-1:-1]
    # print(n2)
    # print(n2)
    if n1==n2:
        print("Palindrome")
    else:
        print("Not a palindrome")
palindrome("nurses run")