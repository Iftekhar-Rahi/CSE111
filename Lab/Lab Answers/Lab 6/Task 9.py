class Student:
    total_s=0
    bracu_s=0
    other_s=0
    @staticmethod
    def printDetails():
        print(f"Total Student(s): {Student.total_s}")
        print(f"BRAC University Student(s): {Student.bracu_s}")
        print(f"Other Institution Student(s): {Student.other_s}")
    def __init__(self,name,dept,uni="Brac University"):
        self.name=name
        self.dept=dept
        self.uni=uni
        Student.total_s+=1
        if self.uni=="Brac University":
            Student.bracu_s += 1
        else:
            Student.other_s += 1
    def individualDetail(self):
        print(f"Name: {self.name}")
        print(f"Department: {self.dept}")
        print(f"Institution: {self.uni}")
    @classmethod
    def createStudent(cls,name,dept,uni="Brac University"):
        obj=cls(name,dept,uni)
        return obj
Student.printDetails()
print('#########################')
mikasa = Student('Mikasa Ackerman', "CSE")
mikasa.individualDetail()
print('------------------------------------------')
Student.printDetails()
print('========================')
harry = Student.createStudent('Harry Potter', "Defence Against Dark Arts", "Hogwarts School")
harry.individualDetail()
print('-------------------------------------------')
Student.printDetails()
print('=========================')
levi = Student.createStudent("Levi Ackerman", "CSE")
levi.individualDetail()
print('--------------------------------------------')
Student.printDetails()