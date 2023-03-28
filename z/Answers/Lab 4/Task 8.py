class ParcelKoro:
    def __init__(self,name="No name set",weight=0,fee=0):
        self.name=name
        self.product_weight=weight
        self.fee=fee
        self.location=None
        self.total=0
    def calculateFee(self,loc=None):
        self.location=loc
        self.total += (self.product_weight * 20)
        if self.total!=0:
            if self.location == None:
                self.total += 50
            else:
                self.total += 100
    def printDetails(self):
        print(f"Customer Name: {self.name}")
        print(f"Product Weight: {self.product_weight}")
        print(f"Total fee: {self.total}")
print("**********************")
p1 = ParcelKoro()
p1.calculateFee()
p1.printDetails()
print("**********************")
p2 = ParcelKoro('Bob The Builder')
p2.calculateFee()
p2.printDetails()
print("----------------------------")
p2.product_weight = 15
p2.calculateFee()
p2.printDetails()
print("**********************")
p3 = ParcelKoro('Dora The Explorer', 10)
p3.calculateFee('Dhanmondi')
p3.printDetails()