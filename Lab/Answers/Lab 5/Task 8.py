class Library:
    def __init__(self,name,book):
        self.name=name
        self.d_books=book
        self.d_borrower={}
    def details(self):
        print(f"{self.name} Library details")
        print("Borrower details:")
        print(self.d_borrower)
        print("Books availability:")
        print(self.d_books)
class Reader:
    def __init__(self,name):
        self.name=name
        self.d_borrower={}
    def borrow(self,library,*args):
        for i in args:
            if library.d_books[i]==0:
                print("Politics books are not available at the moment.")
            else:
                if i not in self.d_borrower:
                    self.d_borrower[i]=1
                    library.d_books[i] = library.d_books[i] - 1
                    print(f"{i} book is borrowed successfully.")
                else:
                    if sum(self.d_borrower.values())<5:
                        # print(sum(self.d_borrower.values()))
                        self.d_borrower[i]=self.d_borrower[i]+1
                        library.d_books[i] = library.d_books[i] - 1
                        print(f"{i} book is borrowed successfully.")
                    else:
                        print("You cannot borrow more than 5 books.")
        library.d_borrower[self.name]=sum(self.d_borrower.values())
    def readerInfo(self,*args):

        if len(args)==0:
            print(f"{self.name}, you have {sum(self.d_borrower.values())} book(s) with you.")
            for key,value in self.d_borrower.items():
                print(f"Books on {key}: {value}")

        else:
            for key, value in self.d_borrower.items():
                for i in args:
                    if key==i:
                        print(f"{self.name}, you have {value} {key} book(s) with you.")
L1=Library('Dhaka',{'Arts':15,'Fiction':135,'Politics':2,'Science':11,'Poetry':15})
L1.details()
print("1----------------------")
r1=Reader('Aladdin')
r1.borrow(L1,'Arts','Fiction','Fiction','Politics')
print("2----------------------")
r1.borrow(L1,'Politics','Fiction')
print("3----------------------")
r1.readerInfo()
print("4----------------------")
r1.readerInfo('Fiction')
print("5----------------------")
L1.details()
print("6----------------------")
r2=Reader('Jasmine')
r2.borrow(L1,'Politics','Poetry')
print("7----------------------")
r2.readerInfo()
print("8----------------------")
L1.details()

