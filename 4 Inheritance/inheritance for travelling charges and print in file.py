#wapp with class trip with class variable person id ,name,age. use constructor to initialize the value
#and def printinfo(self). create another class cash travelling that extends trip class. use class
#variable as a km and a def calculateamount(self);if km>300 20rs/km 2]km>200 & <300 17rs/km else 15rs.
#create another class credit transport that extends trip class with class variable age and def
# calculateamount with following cond-
#1]age>60 450rs charges
#2]age 30-60 280rs else 200.
#store the information about cash transaction into cash.txt and info abt credit
#transaction store in credit.txt and print where is maximum buissness found.cash or credit.
class trip:
    id=0
    name=" "
    age=0
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age
    def print_info(self):
        print("Traveller id :",self.id)
        print("Traveller name",self.name)
        print("TRaveller age",self.age)
class cash_travelling(trip):
    km=0
    def _init_(self,id,name,km):
        super().__init__(id,name)
        self.km=km
    def calculate_amount(self):
        if self.km>300:
            total=20*self.km
        elif self.km>200 and self.km<300:
            total=17*self.km
        else:
            total=15*self.km
        print("Charges by km :",total)
class credit_transport(trip):
    def _init_(self,id,name,age):
        super()._init_(id,name)
    def amount(self):
        if self.age>60:
            total1=450
        elif self.age>30 and self.age<60:
            total1=280
        else:
            total1=200
        print("Charges by age",total1)
id=int(input('ENTER ID'))
name=input("ENTER NAME=")
age=int(input('ENTER AGE='))
km=int(input('ENTER KM='))
obj=cash_travelling(id,name,km)
obj.print_info()
obj.calculate_amount()
obj1=credit_transport(id,name,age)
obj1.amount()







            
