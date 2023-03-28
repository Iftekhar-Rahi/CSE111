class Student:
    def __init__(self,name,id,dept):
        self.name=name
        self.id=id
        self.dept=dept
        self.mylist=[]
    def details(self):
        return (f"Name: {self.name}\nID: {self.id}\nDepartment: {self.dept}")
    def advise(self,*args):
        self.mylist=list(args)
        print(f"{self.name}, you have taken {float(3*len(self.mylist))} credits. \nList of courses: {','.join(self.mylist)}")
        if (3*len(self.mylist))==9:
            print("Status: Ok")
        elif (3*len(self.mylist))>=12:
            print(f"Status: You have to drop at least {int(((3*len(self.mylist))-12)/3)} course.")
        elif (3*len(self.mylist))<=9:
            print(f"Status: You have to take at least {int((9-(3*len(self.mylist)))/3)} more course.")

s1 = Student("Alice","20103012","CSE")
s2 = Student("Bob", "18301254","EEE")
s3 = Student("Carol", "17101238","CSE")
print("##########################")
print(s1.details())
print("##########################")
print(s2.details())
print("##########################")
s1.advise("CSE110", "MAT110", "PHY111")
print("##########################")
s2.advise("BUS101", "MAT120")
print("##########################")
s3.advise("MAT110", "PHY111", "ENG102",
"CSE111", "CSE230")