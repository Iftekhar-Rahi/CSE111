class Exam:
    def __init__(self, marks):
        self.marks = marks
        self.time = 60
    def examSyllabus(self):
        return "Maths , English"
    def examParts(self):
        return "Part 1 - Maths\nPart 2 - English\n"
class ScienceExam(Exam):
    number=2
    def __init__(self,mark,minute,*args):
        super().__init__(mark)
        ScienceExam.number = 2
        self.time = minute
        ScienceExam.number+=len(args)
        self.clist=list(args)
    def examSyllabus(self):
        s=' , '.join(self.clist)
        return f"{super().examSyllabus()} , {s}"
    def examParts(self):
        s = ""
        c = 3
        for i in self.clist:
            s += f"Part{c} - {i}\n"
            c += 1
        # s='\n'.join(self.clist)
        return f"{super().examParts()}{s[:-1]}"
    def __str__(self):

        return f"Marks: {self.marks} Time: {self.time} minutes Number of Parts: {ScienceExam.number}"
engineering = ScienceExam(100, 90, "Physics", "HigherMaths")
print(engineering)
print('----------------------------------')
print(engineering.examSyllabus())
print(engineering.examParts())
print('==================================')
architecture = ScienceExam(100, 120, "Physics", "HigherMaths", "Drawing")
print(architecture)
print('----------------------------------')
print(architecture.examSyllabus())
print(architecture.examParts())
