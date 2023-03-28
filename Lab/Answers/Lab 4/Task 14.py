class StudentDatabase:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        self.grades = {}
        self.season=None
        self.gpa=0
        self.inside = {}
        self.sub_list = []
        self.mark_list = []
    def calculateGPA(self,courses,season):
        self.inside = {}
        self.sub_list = []
        self.mark_list = []
        for i in courses:
            key,value=i.split(": ")
            value = float(value)
            self.season=season
            self.sub_list.append(key)
            self.mark_list.append(value)
        self.gpa = sum(self.mark_list) / len(self.mark_list)
        self.inside[tuple(self.sub_list)] = round(self.gpa,2)
        self.grades[self.season] = self.inside
    def printDetails(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        for k,v in self.grades.items():
            print(f"Courses taken in {k}:")
            for key,value in v.items():
                for i in key:
                    print(i)
                print(f"GPA: {value}")
s1 = StudentDatabase('Pietro', '10101222')
s1.calculateGPA(['CSE230: 4.0', 'CSE220: 4.0', 'MAT110: 4.0'], 'Summer2020')
s1.calculateGPA(['CSE250: 3.7', 'CSE330: 4.0'], 'Summer2021')
print(f'Grades for {s1.name}\n{s1.grades}')
print('------------------------------------------------------')
s1.printDetails()
s2 = StudentDatabase('Wanda', '10103332')
s2.calculateGPA(['CSE111: 3.7', 'CSE260: 3.7', 'ENG101: 4.0'], 'Summer2022')
print('------------------------------------------------------')
print(f'Grades for {s2.name}\n{s2.grades}')
print('------------------------------------------------------')
s2.printDetails()
