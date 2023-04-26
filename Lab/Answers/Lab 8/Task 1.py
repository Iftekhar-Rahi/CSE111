# Task 1
class RealNumber:

    def __init__(self, r=0):
        self.__realValue = r

    def getRealValue(self):
        return self.__realValue

    def setRealValue(self, r):
        self.__realValue = r

    def __str__(self):
        return 'RealPart: ' + str(self.getRealValue())


class ComplexNumber(RealNumber):
    def __init__(self, real=1.0, imagine=1.0):
        super().__init__(real)
        self.imagine = imagine

    def __str__(self):
        s = super().__str__()
        s += f"\nImaginaryPart: {self.imagine}"
        return s


cn1 = ComplexNumber()
print(cn1)
print('---------')
cn2 = ComplexNumber(5, 7)
print(cn2)