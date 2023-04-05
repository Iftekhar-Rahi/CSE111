class Travel:
    count=0
    def __init__(self,start,end):
        self.start=start
        self.end=end
        self.time=1
        Travel.count+=1
    def display_travel_info(self):
        s=f"Source: {self.start}\n"
        s+=f"Destination: {self.end}\n"
        s+=f"Flight Time: {self.time:.2f}"
        return s
    def set_time(self,x):
        self.time = x
    def set_destination(self,x):
        self.end = x
    def set_source(self,x):
        self.start =x
print("No. of Traveller =", Travel.count)
print("=======================")
t1 = Travel("Dhaka","India")
print(t1.display_travel_info())
print("=======================")
t2 = Travel("Kuala Lampur","Dhaka")
t2.set_time(23)
print(t2.display_travel_info())
print("=======================")
t3 = Travel("Dhaka","New_Zealand")
t3.set_time(15)
t3.set_destination("Germany")
print(t3.display_travel_info())
print("=======================")
t4 = Travel("Dhaka","India")
t4.set_time(9)
t4.set_source("Malaysia")
t4.set_destination("Canada")
print(t4.display_travel_info())
print("=======================")
print("No. of Traveller =", Travel.count)
