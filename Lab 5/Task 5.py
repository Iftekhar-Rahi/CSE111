# Task 5
class Student:
    def __init__(self, name, id, dept):
        self.__name = None
        self.__id = None
        self.__dept = None
        self.email = None
        self.password = None
        self.status = None
        self.course = []
        self.setName(name)
        self.setID(id)
        self.setdept(dept)
        print("Student object is created!")

    def setName(self, name):
        self.__name = name

    def setID(self, id):
        self.__id = id

    def setdept(self, dept):
        self.__dept = dept

    # def getlist(self):
    #   return self.__course
    def getname(self):
        return self.__name

    def getID(self):
        return self.__id

    def getdept(self):
        return self.__dept


class Usis:
    def __init__(self):
        print("USIS is ready to use!")

    def login(self, location):
        if location.email == None and location.password == None:
            print("Email and password need to be set.")
        else:
            location.status = "Yes"
            print("Login successful!")

    def advising(self, location, *args):
        if location.status == None:
            print("Please login to advise courses!")
        else:
            if len(args) == 0:
                print("You haven't selected any courses.")
            elif len(args) > 3:
                print("You need special approval to take more than 3 courses.")
            else:
                for i in args:
                    location.course.append(i)
                print("Advising successful!")

    def individualDetails(self, location):
        a = f"Name: {location.getname()}\n"
        b = f"ID:{location.getID()}\n"
        c = f"Department: {location.getdept()}\n"
        d = f"Advised courses: {','.join(location.course)}\n"
        return a + b + c + d


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
