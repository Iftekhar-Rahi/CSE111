class Hotel:
    def __init__(self,h_name):
        self.h_name=h_name
        self.stuff=0
        self.guest=0
        self.s_dic={}
        self.g_dic={}
    def addStuff(self,name,age,phn="000"):
        self.s_name=name
        self.s_age=age
        self.s_phn=phn
        self.stuff+=1
        self.s_dic[self.stuff]=[self.s_name]
        self.s_dic[self.stuff].append(self.s_age)
        self.s_dic[self.stuff].append(self.s_phn)
        print(f"Staff With ID {self.stuff} is added")
    def addGuest(self,name,age,phn):
        self.g_name = name
        self.g_age = age
        self.g_phn = phn
        self.guest+=1
        self.g_dic[self.guest]=[self.g_name]
        self.g_dic[self.guest].append(self.g_age)
        self.g_dic[self.guest].append(self.g_phn)
        print(f"Guest With ID {self.guest} is created")
    def getStuffById(self,key):
        return f"Staff ID: {key} \nName: {self.s_dic[key][0]} \nAge: {self.s_dic[key][1]} \nPhone no.: {self.s_dic[key][2]}"
    def getGuestById(self,key):
        return f"Guest ID: {key} \nName: {self.g_dic[key][0]} \nAge: {self.g_dic[key][1]} \nPhone no.: {self.g_dic[key][2]}"
    def allStaffs(self):
        print("All Staffs:")
        print(f"Number of Staff: {len(list(self.s_dic.keys()))}")
        for i in self.s_dic.keys():
            print(f"Guest ID: {i} Name: {self.s_dic[i][0]} Age: {self.s_dic[i][1]} Phone no.: {self.s_dic[i][2]}")
    def allGuest(self):
        print("All Guest:")
        print(f"Number of Staff: {len(list(self.g_dic.keys()))}")
        for i in self.g_dic.keys():
            print(f"Guest ID: {i} Name: {self.g_dic[i][0]} Age: {self.g_dic[i][1]} Phone no.: {self.g_dic[i][2]}")
h = Hotel("Lakeshore")
h.addStuff( "Adam", 26)
print("=================================")
print(h.getStuffById(1))
print("=================================")
h.addGuest("Carol",35,"123")
print("=================================")
print(h.getGuestById(1))
print("=================================")
h.addGuest("Diana", 32, "431")
print("=================================")
print(h.getGuestById(2))
print("=================================")
h.allStaffs()
print("=================================")
h.allGuest()