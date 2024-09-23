#WRITE A PYTHON PROGRAM WITH CLASS BANK WITH CLASS VARIABLE PERSON ID PERSON
#NAME ,ACCOUNT TYPE,OPENING BALANCE,USE CONSTRUCTOR TO INITIALIZE THE VALUE &
#DEF PRINTINFO(SELF)
#DEF WITHDRAW(SELF,AMOUNT)
#DEF DEPOSITE (SELF,AMOUNT)
#DEF PRINT BALANCE(SELF)
#DEF CALC(SELF,DURATION,RATE)
class bank:
    pid=0
    pname=" "
    at=" "
    obal=0
    def __init__ (self,id,name,at,bal):
        self.pid=id
        self.pname=name
        self.at=at
        self.obal=bal
    def printinfo(self):
        print("person id =",self.pid,"person name=",self.pname,"account type=",self.at,"opening balance=",self.obal)
    def withdraw(self,a):
        self.obal=self.obal-a
    def deposit(self,b):
        self.obal=self.obal+b
    def printbal(self):
        print("Total balance=",self.obal)
    def cal(self,d,r):
        si=(self.obal*d*r)/100
        self.obal=self.obal+si
        print(self.obal)
id=int(input("Enter the account id"))
name=input("Enter the account name")
at=input("Enter the account type")
bal=int(input("Enter the opening balance"))
obj=bank(id,name,at,bal)
a=int(input("Enter the withdraw amount"))
b=int(input("Enter the deposite amount"))
d=int(input("Enter the duration in years"))
r=float(input("Enter rate in per"))
obj.printinfo()
obj.withdraw(a)
obj.deposit(b)
obj.printbal()
obj.cal(d,r)







        
