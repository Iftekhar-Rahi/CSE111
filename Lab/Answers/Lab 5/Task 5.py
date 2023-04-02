class Student:
    def __init__(self,name,id,dept):
        self.name=name
        self.id=id
        self.dept=dept
        self.email=None
        self.password=None
        self.status=None
        self.clist=[]
        print("Student object is created!")
class Usis:
    def __init__(self):
        print("USIS is ready to use!")
    def login(self,location):
        if location.email==None and location.password==None:
            print("Email and password need to be set.")
        elif location.email!=None and location.password!=None:
            location.status="OK"
            print("Login successful!")

    def advising(self,location,*args):
        if location.status==None:
            print("Please login to advise courses!")
        elif location.status!=None and len(args)==0:
            print("You haven't selected any courses.")
        elif len(args)>3:
            print("You need special approval to take more than 3 courses.")
        else:
            print("Advising successful!")
            for i in args:
                location.clist.append(i)
    def individualDetails(self,location):
        print(f"Name: {location.name}")
        print(f"ID : {location.id}")
        print(f"Department : {location.dept}")
        print("Advised courses:",end="")
        print(f"{','.join(location.clist)}")
rakib = Student("Rakib", 12301455, "CSE")
print("1***********************")
usis_obj = Usis()
print("2***********************")
usis_obj.login(rakib)
print("3***********************")
usis_obj.advising(rakib)
print("4***********************")
rakib.email = "rakib@hotmail.com"
rakib.password = "1234"
print("5***********************")
usis_obj.login(rakib)
print("6***********************")
usis_obj.advising(rakib)
print("7***********************")
usis_obj.advising(rakib, "CSE110", "PHY111", "MAT110", "CSE260")
print("8***********************")
usis_obj.advising(rakib, "CSE110", "PHY111", "MAT110")
print("9***********************")
print(usis_obj.individualDetails(rakib))
