class box:
    def __init__(self,mylist):
        print("Creating a box!")
        mylist=list(mylist)
        height =mylist[0]
        width=mylist[1]
        breadth=mylist[2]
        self.height=height
        self.width=width
        self.breadth=breadth
        print(f"Volume of the box is {self.height*self.width*self.breadth} cubic units.")
print("Box 1")
b1 = box([10,10,10])
print("=========================")
print("Height:", b1.height)
print("Width:", b1.width)
print("Breadth:", b1.breadth)
print("-------------------------")
print("Box 2")
b2 = box((30,10,10))
print("=========================")
print("Height:", b2.height)
print("Width:", b2.width)
print("Breadth:", b2.breadth)
b2.height = 300
print("Updating Box 2!")
print("Height:", b2.height)
print("Width:", b2.width)
print("Breadth:", b2.breadth)
print("-------------------------")
print("Box 3")
b3 = b2
print("Height:", b3.height)
print("Width:", b3.width)
print("Breadth:", b3.breadth)
