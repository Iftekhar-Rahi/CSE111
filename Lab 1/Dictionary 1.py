#Dictionary_1
s1 = input().split(', ')
d1={}
for i in s1:
    key, value = tuple(i.split(': '))
    d1[key] = int(value)
s2 = input().split(', ')
d2={}
for i in s2:
    key, value = tuple(i.split(': '))
    d2[key] = int(value)
d3={}
for i in list(d1.keys()):
  if i in list(d2.keys()):
    d3[i]=d1[i]+d2[i]
  else:
    d3[i]=d1[i]
for i in list(d2.keys()):
  if i not in list(d3.keys()):
    d3[i]=d2[i]
print(d3)
x=tuple(d3.values())
y=set(x)
print(f"values: {tuple(sorted(y))}")