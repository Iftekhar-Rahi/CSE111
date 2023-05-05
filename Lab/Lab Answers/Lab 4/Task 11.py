class Author:
    def __init__(self,name="Default",*books):
        self.name=name
        self.book = books
        # if len(args)==0:
        #     self.name = "Default"
        # elif len(args)==1:
        #     self.name = args[0]
        # elif len(args)!=1:
        #     self.book = args[1:]


    def addBooks(self,*args):
        self.book=args
    def printDetails(self):
        print(f"Author Name:  {self.name}")
        print("--------")
        print("List of Books:")
        for i in self.book:
            print(i)
    def changeName(self,nam):
        self.name = nam


auth1 = Author('Humayun Ahmed')
auth1.addBooks('Deyal', 'Megher Opor Bari')
auth1.printDetails()
print('===================')
auth2 = Author()
print(auth2.name)
auth2.changeName('Mario Puzo')
auth2.addBooks('The Godfather', 'Omerta', 'The Sicilian')
print('===================')
auth2.printDetails()
print('===================')
auth3 = Author('Paolo Coelho', 'The Alchemist', 'The Fifth Mountain')
auth3.printDetails()