#dictionary_3
s1 = input().split(', ')
d1={}
new={}
for i in s1:
    key, value = tuple(i.split(' : '))
    d1[key] = value
for k,v in d1.items():
    # if k in list(new.values():
    #     new[v].append(k)
    # else:
    #     new[v] = [k]
    new[v]=[]
for k,v in d1.items():
    new[v].append(k)
# for k,v in d1.items():
#     print(d1.values())
print(new)