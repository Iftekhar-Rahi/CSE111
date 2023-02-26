class TaxiLagbe:
    def __init__(self,number,area):
        self.number=number
        self.area=area
        self.passenger_details=None
        self.passenger_name=None
        self.rate=0
        self.passenger_list=[]
        self.rate_list = []
    def addPassenger(self,*name):
        if len(self.passenger_list)<=3:
            for i in name:
                self.passenger_details = i.split("_")
                self.passenger_name = self.passenger_details[0]
                self.passenger_list.append(self.passenger_name)
                self.rate = int(self.passenger_details[1])
                self.rate_list.append(self.rate)
                print(f"Dear {self.passenger_name}! Welcome to TaxiLagbe.")
        else:
            print("Taxi Full! No more passengers can be added.")
    def printDetails(self):
        print(f"Trip info for Taxi number: {self.number}")
        print(f"This taxi can cover only {self.area} area.")
        print(f"Total passengers: {len(self.passenger_list)}")
        print("Passenger lists:")
        print(','.join(self.passenger_list))
        print(f"Total collected fare: {sum(self.rate_list)} Taka")

taxi1 = TaxiLagbe('1010-01', 'Dhaka')
print('-------------------------------')
taxi1.addPassenger('Walker_100', 'Wood_200')
taxi1.addPassenger('Matt_100')
taxi1.addPassenger('Wilson_105')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi1.addPassenger('Karen_200')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi2 = TaxiLagbe('1010-02', 'Khulna')
taxi2.addPassenger('Ronald_115')
taxi2.addPassenger('Parker_215')
print('-------------------------------')
taxi2.printDetails()
