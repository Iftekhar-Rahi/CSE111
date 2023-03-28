class Library:
    def __init__(self,name,book):
        self.name=name
        self.books=book
        self.borrower={}
    def details(self):
        print(f"{self.name} Library details")
        print("Borrower details:")
        print(self.borrower)
        print("Books availability:")
        print(self.books)
class Reader:
    def __init__(self,name):
        self.name=name

L1=Library('Dhaka',{'Arts':15,'Fiction':135,'Politics':2,'Science':11,'Poetry':15})
L1.details()
print("1----------------------")
#Unfinished