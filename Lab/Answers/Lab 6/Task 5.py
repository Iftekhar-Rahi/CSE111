from datetime import date
class Employee:
    def __init__(self,name,wp):
        self.name=name
        self.workingPeriod=wp
    @classmethod
    def employeeByJoiningYear(cls,name,joining):
        obj=cls(name,date.today().year-joining)
        return obj
    @staticmethod
    def experienceCheck(year,gender):
        if gender=="male":
            pro="He"
        else:
            pro="She"
        if year<3:
            exp="not experienced"
        else:
            exp="experienced"
        return f"{pro} is {exp}"


employee1 = Employee('Dororo', 3)
employee2 = Employee.employeeByJoiningYear('Harry', 2016)
print(employee1.workingPeriod)
print(employee2.workingPeriod)
print(employee1.name)
print(employee2.name)
print(Employee.experienceCheck(2, "male"))
print(Employee.experienceCheck(3, "female"))
