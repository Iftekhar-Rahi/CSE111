# Task 1
class Student:
  ID=0
  def __init__(self,name,dept,age,cgpa):
    self.name=name
    self.dept=dept
    self.age=age
    self.cg=cgpa
    Student.ID+=1
    self.id=Student.ID
  def showDetails(self):
    print(f"ID: {self.id}")
    print(f"Name: {self.name}")
    print(f"Department: {self.dept}")
    print(f"Age: {self.age}")
    print(f"CGPA: {self.cg}")
  @classmethod
  def from_String(cls,details):
    data=details.split("-")
    obj=cls(data[0],data[1],int(data[2]),float(data[3]))
    return obj
s1 = Student("Samin", "CSE", 21, 3.91)
s1.showDetails()
print("-----------------------")
s2 = Student("Fahim", "ECE", 21, 3.85)
s2.showDetails()
print("-----------------------")
s3 = Student("Tahura", "EEE", 22, 3.01)
s3.showDetails()
print("-----------------------")
s4 = Student.from_String("Sumaiya-BBA-23-3.96")
s4.showDetails()