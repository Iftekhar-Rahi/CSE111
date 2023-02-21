def palindromeCheck(seq):
    i = 0
    j = len(seq)-1
    while i<j:
        if seq[i]!=seq[j]:
            return"Not"
            break
        i+=1
        j-=1
    return "yes"
inp = input().lower()
print(palindromeCheck(inp))