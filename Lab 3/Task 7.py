class buttons:
    def __init__(self,word,space,border):
        self.word=word
        self.space=space
        self.border=border
        x=1+self.space+len(self.word)+self.space+1
        print(self.border*x)
        print(self.border, end="")
        print(" " * self.space, end="")
        print(word, end="")
        print(" " * self.space, end="")
        print(self.border)
        print(self.border * x)

word = "CANCEL"
spaces = 10
border = 'x'
b1 = buttons(word, spaces, border)
print("=======================================================")
b2 = buttons("Notify",3, '!')
print("=======================================================")
b3 = buttons('SAVE PROGRESS', 5, '$')
