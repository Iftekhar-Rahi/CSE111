s1 = input().split(', ')
d1={}
#print (string1)
for i in s1:
    #print (index)
    key, value = tuple(i.split(': '))
    # print (key_value)
    d1[key] = int(value)
print (d1)
s2 = input().split(', ')
d2={}
#print (string1)
for i in s2:
    #print (index)
    key, value = tuple(i.split(': '))
    # print (key_value)
    d2[key] = int(value)
print (d2)
# def dictionary_maker(str):
#     str= input().split(', ')
#     dic = {}
#     for i in str:
#         key, value = tuple(i.split(': '))
#         dic[key] = int(value)
#     return dic
# dictionary_maker(a: 100, b: 100, c: 200, d: 300)