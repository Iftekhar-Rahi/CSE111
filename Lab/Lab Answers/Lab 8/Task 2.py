class RealNumber:
    def __init__(self, number=0):
        self.number = number
    def __add__(self, anotherRealNumber):
        return self.number + anotherRealNumber.number
    def __sub__(self, anotherRealNumber):
        return self.number - anotherRealNumber.number
    def __str__(self):
        return str(self.number)
class ComplexNumber (RealNumber):
    def __init__(self,real,i):
        # print(real)
        if isinstance(real,int):
            self.real = real
        else:
            self.real=real.number
        self.imaginary = i

    def __add__(self, anotherComplexNumber):
        return ComplexNumber(self.real + anotherComplexNumber.real, self.imaginary + anotherComplexNumber.imaginary)

    def __sub__(self, anotherComplexNumber):
        return ComplexNumber(self.real - anotherComplexNumber.real, self.imaginary - anotherComplexNumber.imaginary)

    def __str__(self):
        # if self.imaginary >= 0:
            return f"{self.real} + {self.imaginary}i"
        # else:
        #     return f"{self.real} - {abs(self.imaginary)}i"

r1 = RealNumber(3)
r2 = RealNumber(5)
print(r1 + r2)
cn1 = ComplexNumber(2, 1)
print(cn1)
cn2 = ComplexNumber(r1, 5)
print(cn2)
cn3 = cn1 + cn2
print(cn3)
cn4 = cn1 - cn2
print(cn4)
