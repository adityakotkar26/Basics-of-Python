# write a python program with class having a name bank with class veriable accountid person name , account
#type person gender opening date opening balance . use constructor to initialize the value and def
#getbalance (self,) def withroen(self,amount) def deposite(self,amount) def calculate interest(self,duration,rate)
#def print account info (self) throw the exception in following condition .
#if account type not in loan , saving , or current .
#after withdrawing amount balance transfer to the 0 or negative value .
#account opening date greater than current date .
class bank:
    id=0
    name=" "
    gender=" "
    type=" "
    odate=" "
    obalance=0
    def __init__(self,id,name,gender,type,odate,obalance):
        self.id=id
        self.name=name
        self.gender=gender
        self.type=type
        self.odate=odate
        self.obalance=obalance
    def getdetail(self):
        print("person id",self.id)
        print("person name",self.name)
        print("type of account",self.type)
        print("Opening date ",self.odate)
        print("Opening balance",self.obalance)
    def getbalance(self):
        print("current balance",self.balance)
    def withdraw(self,amount):
        rbalance=self.obalance-amount
        print("remaining balance after withdraw amount",rbalance)
    def deposite(self,damount):
        fbalance=self.obalance+damount
        print("Amount with deposite",fbalance)
    def interest(self,duration,rate):
        si=self.obalance*rate*duration/100
        print("Simle Interest ",si)
id1=int(input("Enter the person id"))
name=input("Wntwe the person name")
gender=input("Enter the gender(male/female/trance)")
type=input("Enter the type of account(loan/saving/current)")
odate=input("Enter the opening date")
obalance=int(input("Enter the opening balance"))
obj=bank(id1,name,gender,type,odate,obalance)
num=0
while(num!=0):
    print("Please select")
    print("1.to see the account details")
    print("2.to see ur account balance")
    print("3.to withdraw amount")
    print("4.to deposite amount")
    print("5.to calculate simple interest")
    print("0.exit")
    num=int(input())
    if num==1:
        obj.getdetail()
    elif num==2:
        obj.getbalance()
    elif num==3:
        obj.withdraw(amount)
        amount=int(input("Enter the amount u have to withdraw"))
    elif num==4:
        damount=int(input("Enter the amount u have to deposite"))
        obj.deposite(damount)
    elif num==5:
        rate=int(input("Enter the rate of interest"))
        duration=int(input("Enter the numbe of years"))
        obj.interest(duration,rate)






