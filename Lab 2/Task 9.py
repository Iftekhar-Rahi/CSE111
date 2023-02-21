#Task 9
def proof_reader(name):
    x=".!?"
    name=name[0].upper()+name[1:-1:]
    new=""
    final=""
    counter=[]
    for i in range(len(name)):
        if name[i] in x:
            counter.append(i+2)
        if name[i]==" " and name[i+1]=="i" and name[i+2]==" ":
            new+=" "
            counter.append(i+1)

        else:
            new+=name[i]
    for j in range (len(new)):
        if j in counter:
            final+=new[j].upper()
        else:
            final+=new[j]
    final+="."
    return final
print(proof_reader("Shouldn't i?") )