while True:
    try:
        dic={'1': 'ajs', '2': 'bkt', '3': 'clu', '4': 'dmv', '5': 'enw', '6': 'fox', '7': 'gpy', '8': 'hqz',
                 '9': 'ir'}
        sum=0
        sum2=0
        name=input().lower()
        for i in name:
            for j,k in dic.items():
                if i in k:
                    sum+=int(j)
        while sum>9:
            final=0
            for z in str(sum):
                final+=int(z)
            sum=final
        print(final)
    except:
        break