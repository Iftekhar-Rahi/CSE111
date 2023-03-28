# string_2
inp = input()
number = False
mixed = False
word = False
for i in inp:

    if i.isdigit():
        number = True
        # print("Number")
    elif i.isalpha():
        word = True
        # print("Word")
    else:
        mixed = True
        # print("Mixed")
if number == True and word == True:
    print("MIXED")
elif number == True:
    print("NUMBER")
elif word == True:
    print("WORD")