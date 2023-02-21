def fractioin(n1,n2):
    if n2==0:
        final=0
    else:
        result=n1/n2
        final=result-int(result)
    if final==0:
        final=int(final)
    return final
print(fractioin(0,5))