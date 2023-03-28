class buttons:
    def __init__(self,word,space,border):
        self.word=word
        self.space=space
        self.border=border
        x=1+self.space+len(self.word)+self.space+1
        print(f"{self.word} Button Specifications:")
        print(f"Button name: {word}")
        print(f"Number of the border characters for the top and the bottom: {x}")
        print(f"Number of spaces between the left side border and the first character of the button name: {self.space}")
        print(f"Number of spaces between the right side border and the last character of the button name: {self.space}")
        print(f"Characters representing the borders: {self.border}")
        print()
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
